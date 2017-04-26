from antlr4 import InputStream, CommonTokenStream
from gen.renLexer import renLexer
from gen.renParser import renParser
from gen.renVisitor import renVisitor


class Visitor(renVisitor):
    def visitMoney(self, ctx):
        print "MONEY:", ctx.getText()
        return ctx.getText()

    def visitAnyNumber(self, ctx):
        print "NUMBER:", ctx.getText()
        return ctx.getText()

    def visitAnyDateTime(self, ctx):
        print "DATE:", ctx.getText()
        return ctx.getText()

    def visitWord(self, ctx):
        print "WORD:", ctx.getText()
        return ctx.getText()

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
        return ctx.getText()

    def visitRentuple(self, ctx):
        print "TUPLE:", ctx.getText()
        return ctx.getText()


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
    parse("123")
    parse('640x480')
    parse("abc")
    parse("def")
    parse("75.25")
    parse("1.2e5")
    parse("$79.99")
    parse("3.9%")
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
    parse("1.2")
    parse("#{ffff00}")
    parse("16#{ffff00}")
    parse("64#{aGVsbG8=}")
    parse("127.0.0.1")
    parse("a")
    parse("9")
    parse("+")
