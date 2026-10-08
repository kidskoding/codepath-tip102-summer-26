import pytest
from prob03 import prob03


@pytest.mark.parametrize("key, message, expected", [
    ("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv", "this is a secret"),
    ("eljuxhpwnyrdgtqkviszcfmabo", "hntu depcte lxejw lxwntu zwx piqfx", "find laguna beach behind the grove"),
    ("abcdefghijklmnopqrstuvwxyz", "hello world", "hello world"),
    ("the quick brown fox jumps over the lazy dog", "", ""),
])
def test_prob03(key, message, expected):
    assert prob03(key, message) == expected
