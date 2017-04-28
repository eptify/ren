import pytest
from ren.parser import parse as loads
from ren.ren import stringify as dumps


cases = [
    "[]",
    "#()",
    "123",
    "640x480",
    "abc",
    "def",
    "75.25",
    "1.2e5",
    "$79.99",
    "3.9%",
    "{}",
    '""',
    "none",
    "true",
    "false",
    "yes",
    "no",
    "on",
    "off",
    '{abcd 123}',
    '"hello world"',
    "2013-04-17/18:37:39-06:00",
    "2013-04-17",
    "1.2",
    "#{ffff00}",
    "16#{ffff00}",
    "64#{aGVsbG8=}",
    "127.0.0.1",
    "<tag>",
    "aa",
    "99",
    "a",
    "9",
    "+",
    "a: ",
    "[a 1 2 efg]",
    "#(a: 1 b: 2)",
    '#(a: 1 b: "two")',
]


@pytest.mark.parametrize('s', cases)
def test_ren(s):
    assert dumps(loads(s)) == dumps(loads(dumps(loads(s))))
