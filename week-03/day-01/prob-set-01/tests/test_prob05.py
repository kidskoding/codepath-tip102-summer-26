import pytest
from prob05 import prob05

@pytest.mark.parametrize("post, expected", [
    ("poOost", "post"),
    ("abBAcC", ""),
    ("s", "s"),
    ("", ""),          # empty is already clean
    ("abc", "abc"),    # no removable pairs, unchanged
])
def test_prob05(post, expected):
    assert prob05(post) == expected
