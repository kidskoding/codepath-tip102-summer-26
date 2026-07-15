import pytest
from prob02 import prob02


@pytest.mark.parametrize("sessions, expected", [
    ([(900, 1100), (1300, 1500), (1600, 1800)], 60),
    ([(1000, 1130), (1200, 1300), (1400, 1500)], 30),
    ([(900, 1100), (1115, 1300), (1315, 1500)], 15),
    ([(900, 1000), (1030, 1100)], 30),  # exactly two sessions -> single gap (10:00 -> 10:30 = 30 min)
])
def test_prob02(sessions, expected):
    assert prob02(sessions) == expected
