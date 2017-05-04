from datetime import datetime, timedelta
from decimal import Decimal
from collections import OrderedDict
from base64 import b64encode


class Root(list):
    pass


class Map(OrderedDict):
    pass


class List(list):
    pass


class Tuple(tuple):
    pass


class Word(str):
    pass


class Name(str):
    pass


class ImpliedString(str):
    pass


class Tag(str):
    pass


class Percent(Decimal):
    def __str__(self):
        return super(Percent, self).__str__() + "%"


class Money(Decimal):
    def __str__(self):
        return "$" + super(Money, self).__str__()


class Point(tuple):
    def __str__(self):
        from . import dumps
        return "x".join(map(dumps, self))


class DateTime(datetime):
    pass


class TimeDelta(timedelta):
    pass


class Binary(str):
    def __str__(self):
        return '64#{' + b64encode(self) + '}'
