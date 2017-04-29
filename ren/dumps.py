from collections import Mapping, Iterable
from math import isinf, isnan
from datetime import datetime
from .types import Point, Word


def escape(s):
    s = s.replace('"', '^"')
    s = s.replace('\n', '^/')
    s = s.replace('\r', '^M')
    return s


def dumps(x):
    if x is True:
        return "true"
    if x is False:
        return "false"
    if x is None:
        return "none"
    if isinstance(x, datetime):
        return "{Y}-{M}-{d}/{h}:{m}:{s}".format(
            Y=str(x.year).zfill(4),
            M=str(x.month).zfill(2),
            d=str(x.day).zfill(2),
            h=str(x.hour).zfill(2),
            m=str(x.minute).zfill(2),
            s=str(x.second).zfill(2))
    if isinstance(x, Word):
        return x
    if isinstance(x, basestring):
        return '"' + escape(x) + '"'
    if isinstance(x, Point):
        return str(x)
    if isinstance(x, tuple):
        return ".".join(map(dumps, x))
    if isinstance(x, Mapping):
        return "#(" + " ".join(dumps(Word(k)) + ": " + dumps(v) for k, v in x.iteritems()) + ")"
    if isinstance(x, Iterable):
        return "[" + " ".join(map(dumps, x)) + "]"
    else:
        if isinstance(x, float):
            if isnan(x):
                return "1.#NaN"
            if isinf(x):
                return "1.#INF"
        return str(x)
