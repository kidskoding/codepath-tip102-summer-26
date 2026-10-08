import pytest
from prob03 import prob03


@pytest.mark.parametrize("hunny_jar_sizes, expected", [
    ([5, 3, 2, 4, 1], [1, 2, 3, 4, 5]),
    ([5, 2, 1, 8, 2], [1, 2, 2, 5, 8]),
    ([], []),
    ([7], [7]),
])
def test_prob03(hunny_jar_sizes, expected):
    assert prob03(hunny_jar_sizes) == expected
