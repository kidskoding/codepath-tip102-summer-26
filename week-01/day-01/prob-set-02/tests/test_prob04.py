import pytest
from prob04 import get_last

@pytest.mark.parametrize("arg, expected", [
    (["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"], "black adam"),
    ([], None),
    ([42], 42),  # edge: single element -> that element
])
def test_prob04(arg, expected):
    assert get_last(arg) == expected
