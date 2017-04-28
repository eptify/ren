from collections import Mapping, Iterable
from datetime import datetime, timedelta
from decimal import Decimal
from math import isinf, isnan

class Word(str):
    pass

class Email(object):
    pass

class Url(object):
    pass

class Percent(Decimal):
    def __str__(self):
        return super(Percent, self).__str__() + "%"

class Money(Decimal):
    def __str__(self):
        return "$" + super(Money, self).__str__()

class Point(tuple):
    def __str__(self):
        return "x".join(map(stringify, self))

def escape(s):
    s = s.replace('"', '^"')
    s = s.replace('\n', '^/')
    s = s.replace('\r', '^M')
    return s

def stringify(x):
    if x is True:
        return "true"
    if x is False:
        return "false"
    if x is None:
        return "none"
    if isinstance(x, Word):
        return x
    if isinstance(x, basestring):
        return '"' + escape(x) + '"'
    if isinstance(x, Point):
        return str(x)
    if isinstance(x, tuple):
        return ".".join(map(stringify, x))
    if isinstance(x, Mapping):
        return "#(" + " ".join(stringify(Word(k)) + ": " + stringify(v) for k, v in x.iteritems()) + ")"
    if isinstance(x, Iterable):
        return "[" + " ".join(map(stringify, x)) + "]"
    else:
        if isinstance(x, float):
            if isnan(x):
                return "1.#NaN"
            if isinf(x):
                return "1.#INF"
        return str(x)


if __name__=="__main__":
    print stringify([])
    print stringify({})
    print stringify([Word("a"), 1, True])
    print stringify({"a": 1, "b": "two"})
    print stringify("Ren Example 1")
    print stringify(-42)
    print stringify(98.6)
    print stringify(True)
    print stringify(False)
    print stringify(None)
    print stringify((127, 0, 0, 1))
    print stringify(Point((640, 480)))
    print stringify('abcd: "test"\n 1')
    print stringify(Percent("3.9"))
    print stringify(Money("79.99"))
    print stringify(float('nan'))
    print stringify(float('inf'))
