import pytest
from prob07 import prob07


@pytest.mark.parametrize("visits, expected", [
    (["WeWork", "Regus", "Spaces", "WeWork", "Regus", "WeWork"], ['WeWork']),
    (["IndieDesk", "Spaces", "IndieDesk", "WeWork", "Spaces",
      "IndieDesk", "WeWork"], ['IndieDesk']),
    (["Hub", "Regus", "WeWork", "Hub", "WeWork", "Regus", "Hub",
      "Regus"], ['Hub', 'Regus']),
    (["WeWork"], ['WeWork']),  # single visit
])
def test_prob07(visits, expected):
    assert prob07(visits) == expected
