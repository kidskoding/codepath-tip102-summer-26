import pytest
from prob06 import prob06


@pytest.mark.parametrize("memes, reposts, expected", [
    (["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"], [2, 1, 3],
     ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor",
      "Distracted boyfriend", "One does not simply walk into Mordor", "One does not simply walk into Mordor"]),
    (["Surprised Pikachu", "This is fine", "Expanding brain"], [1, 2, 2],
     ["Surprised Pikachu", "This is fine", "Expanding brain", "This is fine", "Expanding brain"]),
    (["Y U No?", "Philosoraptor"], [3, 1], ["Y U No?", "Philosoraptor", "Y U No?", "Y U No?"]),
    ([], [], []),
])
def test_prob06(memes, reposts, expected):
    assert prob06(memes, reposts) == expected
