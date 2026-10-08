import pytest
from prob02 import prob02


@pytest.mark.parametrize("memes, expected", [
    ([{"creator": "Alex", "text": "Meme 1"}, {"creator": "Jordan", "text": "Meme 2"},
      {"creator": "Alex", "text": "Meme 3"}, {"creator": "Chris", "text": "Meme 4"},
      {"creator": "Jordan", "text": "Meme 5"}], {"Alex": 2, "Jordan": 2, "Chris": 1}),
    ([{"creator": "Sam", "text": "Meme 1"}, {"creator": "Sam", "text": "Meme 2"},
      {"creator": "Sam", "text": "Meme 3"}, {"creator": "Taylor", "text": "Meme 4"}], {"Sam": 3, "Taylor": 1}),
    ([{"creator": "Blake", "text": "Meme 1"}, {"creator": "Blake", "text": "Meme 2"}], {"Blake": 2}),
    ([], {}),
])
def test_prob02(memes, expected):
    assert prob02(memes) == expected
