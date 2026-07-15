import pytest
from prob01 import manage_stage_changes


@pytest.mark.parametrize("changes, expected", [
    (["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"], ["A", "C", "B", "D"]),
    (["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"], []),
    (["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"], ["Z"]),
    ([], []),
    (["Schedule A"], ["A"]),
])
def test_prob01(changes, expected):
    assert manage_stage_changes(changes) == expected
