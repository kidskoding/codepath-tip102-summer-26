import pytest
from prob09 import prob09


@pytest.mark.parametrize("word1, word2, expected", [
    ("wol", "oze", "woozle"),
    ("hfa", "eflump", "heffalump"),
    ("eyre", "eo", "eeyore"),
    ("", "abc", "abc"),
])
def test_prob09(word1, word2, expected):
    assert prob09(word1, word2) == expected
