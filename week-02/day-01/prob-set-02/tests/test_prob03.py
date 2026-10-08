import pytest
from prob03 import prob03


@pytest.mark.parametrize("oxygen_levels, min_val, max_val, expected", [
    ({"Command Module": 21, "Habitation Module": 20, "Laboratory Module": 19, "Airlock": 22, "Storage Bay": 18},
     19, 22, ["Storage Bay"]),
    ({"Airlock": 19, "Storage Bay": 22}, 19, 22, []),  # both bounds are inclusive
    ({}, 19, 22, []),
])
def test_prob03(oxygen_levels, min_val, max_val, expected):
    assert prob03(oxygen_levels, min_val, max_val) == expected
