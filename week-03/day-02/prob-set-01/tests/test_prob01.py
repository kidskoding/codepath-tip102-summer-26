import pytest
from prob01 import prob01


@pytest.mark.parametrize("changes, expected", [
    (["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"], ["A", "C", "B", "D"]),
    (["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"], []),
    (["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"], ["Z"]),
    ([], []),
    (["Schedule A"], ["A"]),
])
def test_prob01(changes, expected):
    assert prob01(changes) == expected
