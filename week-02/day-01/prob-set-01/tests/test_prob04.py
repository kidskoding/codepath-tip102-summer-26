import pytest
from prob04 import prob04


@pytest.mark.parametrize("venue1_schedule, venue2_schedule, expected", [
    ({"Stromae": "9:00 PM", "Janelle Monáe": "8:00 PM", "HARDY": "7:00 PM", "Bruce Springsteen": "6:00 PM"},
     {"Stromae": "9:00 PM", "Janelle Monáe": "10:30 PM", "HARDY": "7:00 PM", "Wizkid": "6:00 PM"},
     {"Stromae": "9:00 PM", "HARDY": "7:00 PM"}),
    ({"Stromae": "9:00 PM"}, {"Wizkid": "9:00 PM"}, {}),
    ({}, {}, {}),
])
def test_prob04(venue1_schedule, venue2_schedule, expected):
    assert prob04(venue1_schedule, venue2_schedule) == expected
