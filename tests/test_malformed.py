import pytest
from ren import loads


cases = [
    '{',
    '{{',
    '{{}',
    '}',
    '{}}',
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
    'a 1',
    'a a',
    '123-123',
    '1a',
]


@pytest.mark.parametrize('case', cases)
def test_malformed(case):
    with pytest.raises(ValueError):
        loads(case)
