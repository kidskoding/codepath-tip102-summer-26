import pytest
from prob01 import prob01


@pytest.mark.parametrize("word1, word2, expected", [
    (["bat", "man"], ["b", "atman"], True),
    (["alfred", "pennyworth"], ["alfredpenny", "word"], False),
    (["cat", "wom", "an"], ["catwoman"], True),
])
def test_prob01(word1, word2, expected):
    assert prob01(word1, word2) == expected
