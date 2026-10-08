import pytest
from prob07 import prob07

COLLAB = {
    "Leonardo DiCaprio": [("Brad Pitt", 40), ("Robert De Niro", 30)],
    "Brad Pitt": [("Leonardo DiCaprio", 40), ("Scarlett Johansson", 20)],
    "Robert De Niro": [("Leonardo DiCaprio", 30), ("Chris Hemsworth", 50)],
    "Scarlett Johansson": [("Brad Pitt", 20), ("Chris Hemsworth", 30)],
    "Chris Hemsworth": [("Robert De Niro", 50), ("Scarlett Johansson", 30)],
}


@pytest.mark.parametrize("a, b, expected", [
    ("Leonardo DiCaprio", "Chris Hemsworth", 90),
    ("Chris Hemsworth", "Leonardo DiCaprio", 90),  # same paths, reversed
    ("Brad Pitt", "Scarlett Johansson", 150),  # long way round beats the direct 20
])
def test_prob07(a, b, expected):
    assert prob07(COLLAB, a, b) == expected
