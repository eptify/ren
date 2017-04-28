from ren import dumps
from ren.types import Word, Point, Percent, Money


print dumps([])
print dumps({})
print dumps([Word("a"), 1, True])
print dumps({"a": 1, "b": "two"})
print dumps("Ren Example 1")
print dumps(-42)
print dumps(98.6)
print dumps(True)
print dumps(False)
print dumps(None)
print dumps((127, 0, 0, 1))
print dumps(Point((640, 480)))
print dumps('abcd: "test"\n 1')
print dumps(Percent("3.9"))
print dumps(Money("79.99"))
print dumps(float('nan'))
print dumps(float('inf'))
