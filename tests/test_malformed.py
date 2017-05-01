import pytest
from ren import loads


cases = [
    '{',
    '{{',
    '{{}',
    '}'
    '#(',
    ')',
    '[',
    ']',
    '1 a',
    '1 1',
    '1.a',
    '#{',
    '"abc',
    '"',
]


@pytest.mark.parametrize('case', cases)
def test_malformed(case):
    with pytest.raises(ValueError):
        loads(case)
