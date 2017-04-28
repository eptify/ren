from datetime import datetime, timedelta
from decimal import Decimal
from collections import OrderedDict


class Map(OrderedDict):
    pass


class List(list):
    pass


class Tuple(tuple):
    pass


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
        from . import dumps
        return "x".join(map(dumps, self))


class DateTime(datetime):
    pass
