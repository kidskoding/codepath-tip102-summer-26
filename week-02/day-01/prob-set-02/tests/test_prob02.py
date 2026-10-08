import pytest
from prob02 import prob02


@pytest.mark.parametrize("planet_name, expected", [
    ("Jupiter", "Planet Jupiter has an orbital period of 10592 Earth days and has 79 moons."),
    ("Pluto", "Sorry, I have no data on that planet."),
    ("Mercury", "Planet Mercury has an orbital period of 88 Earth days and has 0 moons."),
])
def test_prob02(planet_name, expected):
    assert prob02(planet_name) == expected
