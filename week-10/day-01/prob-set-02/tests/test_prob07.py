import pytest
from prob07 import prob07

CELEBS = [
    [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 0
    [0, 1, 1, 0, 0, 0, 0, 0],  # Celeb 1
    [0, 0, 0, 1, 0, 1, 0, 0],  # Celeb 2
    [0, 0, 0, 0, 1, 0, 1, 0],  # Celeb 3
    [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 4
    [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 5
    [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 6
    [0, 0, 0, 0, 1, 0, 1, 0],  # Celeb 7
]


@pytest.mark.parametrize("celebs, start_celeb, target_celeb, expected", [
    (CELEBS, 0, 6, True),               # example
    (CELEBS, 3, 5, False),              # example
    (CELEBS, 5, 0, False),              # edge: nothing connects into celeb 0
    (CELEBS, 2, 5, True),               # edge: direct connection
    ([[0, 1], [0, 0]], 1, 0, False),    # edge: directed edge, wrong way
])
def test_prob07(celebs, start_celeb, target_celeb, expected):
    assert prob07(celebs, start_celeb, target_celeb) == expected
