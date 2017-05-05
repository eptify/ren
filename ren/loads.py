import re
import codecs
from datetime import tzinfo, timedelta

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from .platform import renLexer, renParser, renVisitor, b64decode
from .util import unescape
from .types import (
    Money, Percent, Word, Point, DateTime, TimeDelta, Map,
    List, Tuple, Binary, Name, Root, ImpliedString, Tag
)


def parse_number(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


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
        raise ValueError("unreachable")  # pragma: no cover

    def visitAnyDateTime(self, ctx):
        if ctx.DateTime():
            s = ctx.getText()
            s = s.replace('T', '/')
            if len(s) > 19:
                tz = None
                d = DateTime.strptime(s[:19], "%Y-%m-%d/%H:%M:%S")
                if not s.endswith('Z'):
                    parts = [int(p) for p in s[20:].split(':')]
                    offset = (parts[0] * 60 + parts[1]) * 60
                    sign = s[19]
                    if sign == '-':
                        offset *= -1

                    class TZ(tzinfo):
                        def utcoffset(self, dt):
                            return timedelta(seconds=offset)

                        def dst(self, dt):
                            return timedelta(0)  # pragma: no cover

                        def tzname(self, dt):
                            return sign + ''.join(
                                map(str, parts))  # pragma: no cover

                    tz = TZ()
                d = d.replace(tzinfo=tz)
                return d
            else:
                return DateTime.strptime(s, "%Y-%m-%d/%H:%M:%S")
        elif ctx.Date():
            return DateTime.strptime(ctx.getText(), "%Y-%m-%d")
        elif ctx.RelTime():
            x = dict(zip(('hours', 'minutes', 'seconds'),
                     map(parse_number, ctx.getText().split(':'))))
            return TimeDelta(**x)
        raise ValueError("unreachable")  # pragma: no cover

    def visitWord(self, ctx):
        return Word(ctx.getText())

    def visitAnyString(self, ctx):
        if ctx.String():
            return unescape(ctx.getText()[1:-1])
        elif ctx.MultilineString():
            return ctx.getText()[1:-1].replace('^{', '{').replace('^}', '}')
        elif ctx.ImpliedString():
            return ImpliedString(ctx.getText())
        elif ctx.Tag():
            return Tag(ctx.getText())
        raise ValueError("unreachable")  # pragma: no cover

    def visitPoint(self, ctx):
        return Point(map(parse_number, ctx.getText().split('x')))

    def visitAnyBinary(self, ctx):
        x = re.sub('\s+', '', ctx.getText())
        if ctx.B16binary():
            if x.startswith('16'):
                x = x[4:-1]
            else:
                x = x[2:-1]
            return Binary(codecs.decode(x, 'hex'))
        elif ctx.B64binary():
            x = x[4:-1]
            return Binary(b64decode(x))
        raise ValueError("unreachable")  # pragma: no cover

    def visitLogic(self, ctx):
        if ctx.getText() in ("yes", "on", "true"):
            return True
        return False

    def visitNone(self, ctx):
        return None

    def visitRentuple(self, ctx):
        return Tuple(map(int, ctx.getText().split('.')))

    def visitName(self, ctx):
        return Name(ctx.getText().rstrip()[:-1])

    def visitRenlist(self, ctx):
        return List([self.visit(v) for v in ctx.value()])

    def visitNameValuePair(self, ctx):
        return self.visit(ctx.name()), self.visit(ctx.value())

    def visitRenmap(self, ctx):
        return Map(self.visit(p) for p in ctx.nameValuePair())

    def visitRoot(self, ctx):
        return Root([self.visit(v) for v in ctx.value()])


class RenErrorListener(ErrorListener):
    def __init__(self):
        super(RenErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError("line " + str(line) + ":" + str(column) + " " + msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex,
                        stopIndex, exact, ambigAlts, configs):
        raise ValueError("unreachable")  # pragma: no cover

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex,
                                    stopIndex, conflictingAlts, configs):
        raise ValueError("unreachable")  # pragma: no cover

    def reportContextSensitivity(self, recognizer, dfa, startIndex,
                                 stopIndex, prediction, configs):
        raise ValueError("unreachable")  # pragma: no cover


def loads(s):
    inp = InputStream(s)
    lexer = renLexer(inp)
    lexer._listeners = [RenErrorListener()]
    stream = CommonTokenStream(lexer)
    parser = renParser(stream)
    parser._listeners = [RenErrorListener()]
    tree = parser.root()
    visitor = Visitor()
    return visitor.visit(tree)
