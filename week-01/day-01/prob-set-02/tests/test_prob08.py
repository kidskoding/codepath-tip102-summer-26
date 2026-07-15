import pytest
from prob08 import prob08

@pytest.mark.parametrize("crowd, target, expected", [
    (['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker'], 'The Joker', [1, 4, 6]),
    (['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker'], 'Bane', []),
    ([], 'The Joker', []),
    (['The Joker', 'Batman'], 'The Joker', [0]),
])
def test_prob08(crowd, target, expected):
    assert prob08(crowd, target) == expected
