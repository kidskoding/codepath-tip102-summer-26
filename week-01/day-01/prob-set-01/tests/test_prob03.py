import pytest
from prob03 import print_catchphrase

@pytest.mark.parametrize("name, expected", [
    ("Pooh", "Oh bother!"),
    ("Tigger", "TTFN: Ta-ta for now!"),
    ("Eeyore", "Thanks for noticing me."),
    ("Christopher Robin", "Silly old bear."),
    ("Piglet", "Sorry! I don't know Piglet's catchphrase!"),
    # edge: lookup is case-sensitive, "pooh" != "Pooh" -> unknown
    ("pooh", "Sorry! I don't know pooh's catchphrase!"),
])
def test_prob03(name, expected):
    assert print_catchphrase(name) == expected
