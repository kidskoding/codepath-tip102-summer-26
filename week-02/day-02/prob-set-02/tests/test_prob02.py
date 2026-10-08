import pytest
from prob02 import prob02


@pytest.mark.parametrize("souvenirs, expected", [
    (["keychain", "hat", "hat", "keychain", "keychain", "postcard"], True),
    (["postcard", "postcard", "postcard", "postcard"], True),
    (["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"], False),
    (["hat", "hat", "magnet", "magnet"], False),
])
def test_prob02(souvenirs, expected):
    assert prob02(souvenirs) == expected
