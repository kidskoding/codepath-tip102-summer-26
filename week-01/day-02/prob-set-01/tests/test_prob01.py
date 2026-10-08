import pytest
from prob01 import prob01


@pytest.mark.parametrize("sentence, expected", [
    ("tubby little cubby all stuffed with fluff", "fluff with stuffed all cubby little tubby"),
    ("Pooh", "Pooh"),
    ("hunny pot", "pot hunny"),
])
def test_prob01(sentence, expected):
    assert prob01(sentence) == expected
