from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from gen.renLexer import renLexer
from gen.renParser import renParser
from gen.renVisitor import renVisitor
from .types import Money, Percent, Word, Point, DateTime, Map, List, Tuple


def parse_number(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def unescape(s):
    return s


class Visitor(renVisitor):
    def visitAnyNumber(self, ctx):
        if ctx.Money():
            return Money(ctx.getText().lstrip("$"))
        elif ctx.Number():
            return parse_number(ctx.getText())
        elif ctx.Percent():
            return Percent(ctx.getText().rstrip("%"))
        elif ctx.NAN():
            return float('nan')
        elif ctx.INF():
            return float('inf')
        return ctx.getText()

    def visitAnyDateTime(self, ctx):
        if ctx.DateTime():
            pass
        elif ctx.Date():
            return DateTime.strptime(ctx.getText(), "%Y-%m-%d")
        return ctx.getText()

    def visitWord(self, ctx):
        return Word(ctx.getText())

    def visitAnyString(self, ctx):
        if ctx.String():
            return unescape(ctx.getText()[1:-1])
        return ctx.getText()

    def visitPoint(self, ctx):
        return Point(map(parse_number, ctx.getText().split('x')))

    def visitAnyBinary(self, ctx):
        if ctx.B16binary():
            pass
        elif ctx.B64binary():
            pass
        return ctx.getText()

    def visitLogic(self, ctx):
        if ctx.getText() in ("yes", "on", "true"):
            return True
        return False

    def visitNone(self, ctx):
        return None

    def visitRentuple(self, ctx):
        return Tuple(map(int, ctx.getText().split('.')))

    def visitName(self, ctx):
        return ctx.getText()[:-2]

    def visitRenlist(self, ctx):
        return List([self.visit(v) for v in ctx.value()])

    def visitNameValuePair(self, ctx):
        return self.visit(ctx.name()), self.visit(ctx.value())

    def visitRenmap(self, ctx):
        return Map(self.visit(p) for p in ctx.nameValuePair())

    def visitSingleValue(self, ctx):
        return self.visit(ctx.value())


class RenErrorListener(ErrorListener):
    def __init__(self):
        super(RenErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError("line " + str(line) + ":" + str(column) + " " + msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise ValueError("ambiguity")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise ValueError("attempting full context")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise ValueError("context sensitivity")


def loads(s):
    inp = InputStream(s)
    lexer = renLexer(inp)
    lexer._listeners = [RenErrorListener()]
    stream = CommonTokenStream(lexer)
    parser = renParser(stream)
    parser._listeners = [RenErrorListener()]
    tree = parser.singleValue()
    visitor = Visitor()
    return visitor.visit(tree)