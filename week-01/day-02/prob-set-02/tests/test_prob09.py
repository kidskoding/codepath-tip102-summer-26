import pytest
from prob09 import prob09


@pytest.mark.parametrize("lst1, lst2, expected", [
    (["super strength", "super speed", "x-ray vision"],
     ["super speed", "time travel", "dimensional travel"], ["super speed"]),
    (["super strength", "super speed", "x-ray vision"],
     ["martial arts", "stealth", "master detective"], []),
    ([], ["stealth"], []),
])
def test_prob09(lst1, lst2, expected):
    assert prob09(lst1, lst2) == expected
