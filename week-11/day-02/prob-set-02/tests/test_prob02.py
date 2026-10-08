import copy

import pytest
from prob02 import prob02


@pytest.mark.parametrize("kingdom, expected", [
    ([["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]], True),
    ([["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]], True),
    ([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]], False),
    ([["a", "a"], ["a", "a"]], True),  # smallest possible cycle, length 4
    ([["a", "a", "a"]], False),  # a straight line can't loop back
])
def test_prob02(kingdom, expected):
    assert prob02(copy.deepcopy(kingdom)) == expected
