from collections import Mapping, Iterable
from math import isinf, isnan
from datetime import datetime, timedelta
from .types import Point, Word, Binary, Name, Root, ImpliedString, Tag
from .util import escape


def dumps(x):
    if x is True:
        return "true"
    if x is False:
        return "false"
    if x is None:
        return "none"
    if isinstance(x, Root):
        return " ".join(map(dumps, x))
    if isinstance(x, Binary):
        return str(x)
    if isinstance(x, datetime):
        return "{Y}-{M}-{d}/{h}:{m}:{s}".format(
            Y=str(x.year).zfill(4),
            M=str(x.month).zfill(2),
            d=str(x.day).zfill(2),
            h=str(x.hour).zfill(2),
            m=str(x.minute).zfill(2),
            s=str(x.second).zfill(2))
    if isinstance(x, timedelta):
        return str(x)
    if isinstance(x, Name):
        return x + ": "
    if isinstance(x, Word):
        return x
    if isinstance(x, ImpliedString):
        return x
    if isinstance(x, Tag):
        return x
    if isinstance(x, basestring):
        return '"' + escape(x) + '"'
    if isinstance(x, Point):
        return str(x)
    if isinstance(x, tuple):
        return ".".join(map(dumps, x))
    if isinstance(x, Mapping):
        return "#(" + " ".join(dumps(Name(k)) + dumps(v) for k, v in x.iteritems()) + ")"
    if isinstance(x, Iterable):
        return "[" + " ".join(map(dumps, x)) + "]"
    else:
        if isinstance(x, float):
            if isnan(x):
                return "1.#NaN"
            if isinf(x):
                return "1.#INF"
        return str(x)
