from prob04 import get_last

def test_prob04():
    assert get_last(
        ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
    ) == "black adam"
    assert get_last([]) is None
