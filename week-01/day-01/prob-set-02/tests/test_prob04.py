import pytest
from prob04 import prob04

@pytest.mark.parametrize("arg, expected", [
    (["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"], "black adam"),
    ([], None),
    ([42], 42),  # edge: single element -> that element
])
def test_prob04(arg, expected):
    assert prob04(arg) == expected
