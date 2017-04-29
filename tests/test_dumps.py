from ren import dumps
from ren.types import Word, Point, Percent, Money

cases = [
    [],
    {},
    [Word("a"), 1, True],
    {"a": 1, "b": "two"},
    "Ren Example 1",
    -42,
    98.6,
    True,
    False,
    None,
    (127, 0, 0, 1),
    Point((640, 480)),
    'abcd: "test"\n 1',
    Percent("3.9"),
    Money("79.99"),
    float('nan'),
    float('inf'),
]


for case in cases:
    print dumps(case)
