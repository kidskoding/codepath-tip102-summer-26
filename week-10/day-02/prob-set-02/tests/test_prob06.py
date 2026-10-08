import pytest
from prob06 import prob06


@pytest.mark.parametrize("celebrities, expected", [
    ({"Dev Patel": ["Meryl Streep", "Viola Davis"],
      "Meryl Streep": ["Dev Patel", "Viola Davis"],
      "Viola Davis": ["Meryl Streep", "Dev Patel"]}, True),
    ({"John Cho": ["Rami Malek", "Zoe Saldana", "Meryl Streep"],
      "Rami Malek": ["John Cho", "Zoe Saldana", "Meryl Streep"],
      "Zoe Saldana": ["Rami Malek", "John Cho", "Meryl Streep"],
      "Meryl Streep": []}, False),
    ({"Dev Patel": ["Meryl Streep"], "Meryl Streep": ["Dev Patel"]}, True),
    ({"Dev Patel": ["Meryl Streep"], "Meryl Streep": []}, False),  # one-way like
    ({"Dev Patel": []}, True),  # a single celebrity
])
def test_prob06(celebrities, expected):
    assert prob06(celebrities) == expected
