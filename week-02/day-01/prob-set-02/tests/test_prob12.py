import pytest
from prob12 import prob12


@pytest.mark.parametrize("paths, expected", [
    ([["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]], "Europa"),
    ([["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]], "Delta"),
    ([["StationA", "StationZ"]], "StationZ"),
])
def test_prob12(paths, expected):
    assert prob12(paths) == expected
