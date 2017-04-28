from antlr4 import InputStream, CommonTokenStream
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
            print "MONEY"
            return Money(ctx.getText().lstrip("$"))
        elif ctx.Number():
            print "NUMBER"
            return parse_number(ctx.getText())
        elif ctx.Percent():
            print "PERCENT"
            return Percent(ctx.getText().rstrip("%"))
        elif ctx.NAN():
            print "NAN"
            return float('nan')
        elif ctx.INF():
            print "INF"
            return float('inf')
        print ctx.getText()
        return ctx.getText()

    def visitAnyDateTime(self, ctx):
        print "DATE:", ctx.getText()
        if ctx.DateTime():
            pass
        elif ctx.Date():
            return DateTime.strptime(ctx.getText(), "%Y-%m-%d")
        return ctx.getText()

    def visitWord(self, ctx):
        print "WORD:", ctx.getText()
        return Word(ctx.getText())

    def visitAnyString(self, ctx):
        print "STRING:", ctx.getText()
        if ctx.String():
            return unescape(ctx.getText()[1:-1])
        return ctx.getText()

    def visitPoint(self, ctx):
        print "POINT:", ctx.getText()
        return Point(map(parse_number, ctx.getText().split('x')))

    def visitAnyBinary(self, ctx):
        print "BINARY:", ctx.getText()
        if ctx.B16binary():
            pass
        elif ctx.B64binary():
            pass
        return ctx.getText()

    def visitLogic(self, ctx):
        print "LOGIC:", ctx.getText()
        if ctx.getText() in ("yes", "on", "true"):
            return True
        return False

    def visitNone(self, ctx):
        return None

    def visitRentuple(self, ctx):
        print "TUPLE:", ctx.getText()
        return Tuple(map(int, ctx.getText().split('.')))

    def visitName(self, ctx):
        print "NAME:", ctx.getText()
        return ctx.getText()[:-2]

    def visitRenlist(self, ctx):
        return List([self.visit(v) for v in ctx.value()])

    def visitNameValuePair(self, ctx):
        return self.visit(ctx.name()), self.visit(ctx.value())

    def visitRenmap(self, ctx):
        return Map(self.visit(p) for p in ctx.nameValuePair())


def loads(s):
    inp = InputStream(s)
    lexer = renLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = renParser(stream)
    tree = parser.value()
    visitor = Visitor()
    return visitor.visit(tree)
