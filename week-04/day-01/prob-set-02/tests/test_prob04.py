import pytest
from prob04 import prob04


@pytest.mark.parametrize("memes, expected", [
    (["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
     ["One does not simply walk into Mordor", "Distracted boyfriend", "Dogecoin to the moon!"]),
    (["Surprised Pikachu", "Expanding brain", "This is fine"],
     ["This is fine", "Expanding brain", "Surprised Pikachu"]),
    (["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"],
     ["Bad Luck Brian", "Philosoraptor", "First world problems", "Y U No?"]),
    ([], []),
])
def test_prob04(memes, expected):
    original = list(memes)
    assert prob04(memes) == expected
    assert memes == original  # must return a new list, not reverse the input
