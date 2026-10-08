import pytest
from prob07 import prob07


@pytest.mark.parametrize("transmission, searchSignal, expected", [
    ("i love eating burger", "burg", 4),
    ("this problem is an easy problem", "pro", 2),
    ("i am tired", "you", -1),
    ("burger", "burger", 1),  # whole signal counts as a prefix
])
def test_prob07(transmission, searchSignal, expected):
    assert prob07(transmission, searchSignal) == expected
