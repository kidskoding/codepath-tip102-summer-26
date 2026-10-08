import pytest
from prob01 import prob01


@pytest.mark.parametrize("crew, position, expected", [
    (["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"],
     ["Commander", "Flight Engineer", "Flight Engineer", "Flight Engineer", "Flight Engineer"],
     {"Andreas Mogensen": "Commander", "Jasmin Moghbeli": "Flight Engineer", "Satoshi Furukawa": "Flight Engineer",
      "Loral O'Hara": "Flight Engineer", "Konstantin Borisov": "Flight Engineer"}),
    (["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"],
     ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"],
     {"Michael Lopez-Alegria": "Commander", "Walter Villadei": "Mission Pilot",
      "Alper Gezeravci": "Mission Specialist", "Marcus Wandt": "Mission Specialist"}),
    ([], [], {}),
])
def test_prob01(crew, position, expected):
    assert prob01(crew, position) == expected
