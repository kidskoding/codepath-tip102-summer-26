import pytest
from prob07 import prob07


@pytest.mark.parametrize("memes, target, expected", [
    ([("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)],
     13, ("Distracted boyfriend", "Dogecoin to the moon!")),
    ([("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)],
     10, ("Surprised Pikachu", "Expanding brain")),
    ([("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)],
     12, ("Bad Luck Brian", "First world problems")),
    ([("Philosoraptor", 1), ("Bad Luck Brian", 4)], 100, ("Philosoraptor", "Bad Luck Brian")),
])
def test_prob07(memes, target, expected):
    assert prob07(memes, target) == expected
