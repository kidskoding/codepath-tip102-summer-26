import pytest
from prob07 import prob07


@pytest.mark.parametrize("ecosystem_data, expected", [
    ("f123de34g8hi34", 3),
    ("species1234forest234", 2),
    ("x1y01z001", 1),
    ("abc", 0),
])
def test_prob07(ecosystem_data, expected):
    assert prob07(ecosystem_data) == expected
