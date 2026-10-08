import pytest
from prob02 import prob02

FESTIVAL_SCHEDULE = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"},
}


@pytest.mark.parametrize("artist, festival_schedule, expected", [
    ("Blood Orange", FESTIVAL_SCHEDULE, {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"}),
    ("Taylor Swift", FESTIVAL_SCHEDULE, {"message": "Artist not found"}),
    ("Metallica", {}, {"message": "Artist not found"}),
])
def test_prob02(artist, festival_schedule, expected):
    assert prob02(artist, festival_schedule) == expected
