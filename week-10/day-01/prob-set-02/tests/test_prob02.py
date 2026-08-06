import pytest
from prob02 import prob02


@pytest.mark.parametrize("celebrities, expected", [
    ([[0, 1, 1, 0],
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [0, 0, 1, 0]], True),     # example
    ([[0, 1, 1, 0],
      [1, 0, 0, 0],
      [1, 1, 0, 1],
      [0, 0, 0, 0]], False),    # example
    ([[0]], True),              # edge: single celebrity
    ([[0, 1],
      [0, 0]], False),          # edge: one-sided like
    ([], True),                 # edge: no celebrities
])
def test_prob02(celebrities, expected):
    assert prob02(celebrities) == expected
