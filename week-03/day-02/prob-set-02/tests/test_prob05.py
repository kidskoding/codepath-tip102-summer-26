from prob05 import merge_schedules


def test_prob05():
    assert merge_schedules("abc", "pqr") == "apbqcr"
    assert merge_schedules("ab", "pqrs") == "apbqrs"
    assert merge_schedules("abcd", "pq") == "apbqcd"
