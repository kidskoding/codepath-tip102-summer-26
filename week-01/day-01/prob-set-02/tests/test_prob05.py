import pytest
from prob05 import concatenate

@pytest.mark.parametrize("arg, expected", [
    (["vengeance", "darkness", "batman"], "vengeancedarknessbatman"),
    ([], ""),
    (["batman"], "batman"),  # edge: single element -> itself
])
def test_prob05(arg, expected):
    assert concatenate(arg) == expected
