import pytest
from prob04 import prob04


@pytest.mark.parametrize("text, expected", [
    ("The quick brown fox jumps over the lazy dog. The dog was not amused.",
     ({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1,
       'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}, ['the'])),
    ("Digital nomads love to travel. Travel is their passion.",
     ({'digital': 1, 'nomads': 1, 'love': 1, 'to': 1, 'travel': 2, 'is': 1,
       'their': 1, 'passion': 1}, ['travel'])),
    ("Stay connected. Stay productive. Stay happy.",
     ({'stay': 3, 'connected': 1, 'productive': 1, 'happy': 1}, ['stay'])),
    ("Hello", ({'hello': 1}, ['hello'])),   # single word
    ("Go, go GO!", ({'go': 3}, ['go'])),    # case + punctuation collapse to one word
])
def test_prob04(text, expected):
    assert prob04(text) == expected
