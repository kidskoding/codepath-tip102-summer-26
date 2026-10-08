import pytest
from prob05 import prob05


@pytest.mark.parametrize("operations, expected", [
    (["trouncy", "flouncy", "flouncy"], 2),
    (["bouncy", "bouncy", "flouncy"], 4),
    ([], 1),
    (["pouncy"], 0),
])
def test_prob05(operations, expected):
    assert prob05(operations) == expected
