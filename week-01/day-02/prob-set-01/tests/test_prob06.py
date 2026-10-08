import pytest
from prob06 import prob06


@pytest.mark.parametrize("words, s, expected", [
    (["christopher", "robin", "milne"], "crm", True),
    (["pooh", "bear"], "pb", True),
    (["bear", "pooh"], "pb", False),
])
def test_prob06(words, s, expected):
    assert prob06(words, s) == expected
