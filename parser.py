from antlr4 import InputStream, CommonTokenStream
from gen.renLexer import renLexer
from gen.renParser import renParser
from gen.renVisitor import renVisitor
from collections import OrderedDict
from ren import Money, Percent, Word


class Visitor(renVisitor):
    def visitAnyNumber(self, ctx):
        if ctx.Money():
            print "MONEY"
            return Money(ctx.getText().lstrip("$"))
        elif ctx.Number():
            print "NUMBER"
            try:
                return int(ctx.getText())
            except ValueError:
                return float(ctx.getText())
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
        return ctx.getText()

    def visitWord(self, ctx):
        print "WORD:", ctx.getText()
        return Word(ctx.getText())

    def visitAnyString(self, ctx):
        print "STRING:", ctx.getText()
        return ctx.getText()

    def visitPoint(self, ctx):
        print "POINT:", ctx.getText()
        return ctx.getText()

    def visitAnyBinary(self, ctx):
        print "BINARY:", ctx.getText()
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
        return ctx.getText()

    def visitName(self, ctx):
        print "NAME:", ctx.getText()
        return ctx.getText()

    def visitRenlist(self, ctx):
        return [self.visit(v) for v in ctx.value()]

    def visitNameValuePair(self, ctx):
        return self.visit(ctx.name()), self.visit(ctx.value())

    def visitRenmap(self, ctx):
        return OrderedDict(self.visit(p) for p in ctx.nameValuePair())


def parse(s):
    inp = InputStream(s)
    lexer = renLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = renParser(stream)
    tree = parser.value()
    visitor = Visitor()
    return visitor.visit(tree)


if __name__=="__main__":
    parse("[]")
    parse("#()")
    print parse("123")
    parse('640x480')
    parse("abc")
    parse("def")
    print parse("75.25")
    print parse("1.2e5")
    print parse("$79.99")
    print parse("3.9%")
    parse("{}")
    parse('""')
    parse("none")
    parse("true")
    parse("false")
    parse("yes")
    parse("no")
    parse("on")
    parse("off")
    parse('{abcd 123}')
    parse('"hello world"')
    parse("2013-04-17/18:37:39-06:00")
    parse("2013-04-17")
    print parse("1.2")
    parse("#{ffff00}")
    parse("16#{ffff00}")
    parse("64#{aGVsbG8=}")
    parse("127.0.0.1")
    parse("<tag>")
    parse("aa")
    print parse("99")
    parse("a")
    print parse("9")
    parse("+")
    parse("a: ")
    print parse("[a 1 2 efg]")
    print parse("#(a: 1 b: 2)")
