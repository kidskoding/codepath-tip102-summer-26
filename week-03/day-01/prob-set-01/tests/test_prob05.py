import pytest
from prob05 import content_cleaner

@pytest.mark.parametrize("post, expected", [
    ("poOost", "post"),
    ("abBAcC", ""),
    ("s", "s"),
    ("", ""),          # empty is already clean
    ("abc", "abc"),    # no removable pairs, unchanged
])
def test_prob05(post, expected):
    assert content_cleaner(post) == expected
