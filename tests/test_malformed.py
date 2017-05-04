import pytest
from ren import loads


cases = [
    '',
    '{',
    '{{',
    '{{}',
    '}',
    '{}}',
    '#(',
    ')',
    '[',
    ']',
    '#{',
    '"abc',
    '"',
]


@pytest.mark.parametrize('case', cases)
def test_malformed(case):
    with pytest.raises(ValueError):
        loads(case)
