from collections import Mapping, Iterable
from datetime import datetime, timedelta
from math import isinf, isnan

from .platform import isstr, iteritems
from .types import Point, Word, Binary, Name, Root, ImpliedString, Tag
from .util import escape


def dumps(x):
    if x is True:
        return "true"
    elif x is False:
        return "false"
    elif x is None:
        return "none"
    elif isinstance(x, Root):
        return " ".join(map(dumps, x))
    elif isinstance(x, Binary):
        return str(x)
    elif isinstance(x, datetime):
        return str(x).replace(' ', '/')
    elif isinstance(x, timedelta):
        return str(x)
    elif isinstance(x, Name):
        return x + ": "
    elif isinstance(x, Word):
        return x
    elif isinstance(x, ImpliedString):
        return x
    elif isinstance(x, Tag):
        return x
    elif isstr(x):
        return '"' + escape(x) + '"'
    elif isinstance(x, Point):
        return str(x)
    elif isinstance(x, tuple):
        return ".".join(map(dumps, x))
    elif isinstance(x, Mapping):
        return "#(" + " ".join(
            dumps(Name(k)) + dumps(v) for k, v in iteritems(x)) + ")"
    elif isinstance(x, Iterable):
        return "[" + " ".join(map(dumps, x)) + "]"
    else:
        if isinstance(x, float):
            if isnan(x):
                return "1.#NaN"
            elif isinf(x):
                return "1.#INF"
        return str(x)
