import pytest
from prob03 import prob03


# order of the trending list is not specified, so compare sorted
@pytest.mark.parametrize("memes, expected", [
    (["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!",
      "Distracted boyfriend", "One does not simply walk into Mordor"],
     ["Dogecoin to the moon!", "One does not simply walk into Mordor"]),
    (["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"],
     ["Surprised Pikachu"]),
    (["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"], []),
    ([], []),
])
def test_prob03(memes, expected):
    assert sorted(prob03(memes)) == sorted(expected)
