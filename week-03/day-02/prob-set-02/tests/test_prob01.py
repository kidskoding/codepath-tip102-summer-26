from prob01 import manage_stage_changes


def test_prob01():
    assert manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]) == ["A", "C", "B", "D"]
    assert manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]) == []
    assert manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]) == ["Z"]
