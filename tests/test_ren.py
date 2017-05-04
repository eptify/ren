# -*- coding: utf-8 -*-

import pytest
from ren import dumps, loads


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
    '[]           ; empty list',
    '#()          ; empty map',
    '[a 1 true #three]    ; non-empty list',
    '#(a: 1 b: "two") ; non-empty map',
    '"Ren Example 1"  ; string',
    '-42          ; number',
    '98.6         ; another number',
    'true         ; literal true',
    'false        ; literal false',
    'none         ; literal nil/null/nada',
    u"""#(           ; a bigger map
       quote:    "禅 saying: ^"仁 rocks!^""
       utf-8:    "^(CE91) to ^(cf89)"
       sci-phi:  0.1618e1
       tax-rate: 3.9%
       price:    $79.99
       url:      http://www.ren-data.org/
       email:    info@ren-data.org
       hashtag:  #ren
       date:     2013-04-17/18:37:39-06:00
       warning:  00:02     ; = 00:00:120.0
       ip-addr:  127.0.0.1
       geo-pos:  43.6x116.7x817
       hex:      16#{DECAFBAD CAFE 00FF}
       base-64:  64#{UmVuIGlzIGRhdGE=}
    )""",
    '"abcd: ^"test^"^/ 1"',
    "1.#NaN",
    "1.#INF",
    "#555-555",
    "3.1.2",
    "#123-456",
    "%/path/to/file",
    "example@example.com",
    "http://example.com",
    '{^{^}}',
]


@pytest.mark.parametrize('case', cases)
def test_ren(case):
    assert dumps(loads(case)) == dumps(loads(dumps(loads(case))))


if __name__ == "__main__":
    for case in cases:
        x = loads(case)
        print case, x, dumps(x), type(x[0]).__name__
