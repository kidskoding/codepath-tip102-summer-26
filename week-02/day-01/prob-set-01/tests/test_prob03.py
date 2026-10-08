import pytest
from prob03 import prob03


@pytest.mark.parametrize("ticket_sales, expected", [
    ({"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}, 4500),
    ({}, 0),
])
def test_prob03(ticket_sales, expected):
    assert prob03(ticket_sales) == expected
