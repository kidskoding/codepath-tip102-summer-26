import pytest
from prob08 import prob08


@pytest.mark.parametrize("memes, start_day, end_day, expected", [
    ([{"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
      {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
      {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}], 1, 3, "Dogecoin to the moon!"),
    ([{"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
      {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
      {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}], 0, 2, "This is fine"),
    ([{"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
      {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}], 2, 4, "Philosoraptor"),
    ([{"name": "Y U No?", "reposts": [2, 2]},
      {"name": "Philosoraptor", "reposts": [2, 2]}], 0, 1, "Y U No?"),  # tie: first in list wins
])
def test_prob08(memes, start_day, end_day, expected):
    assert prob08(memes, start_day, end_day) == expected
