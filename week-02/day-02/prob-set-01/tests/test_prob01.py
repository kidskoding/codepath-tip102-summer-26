import pytest
from prob01 import prob01


@pytest.mark.parametrize("species_list, expected", [
    ([{"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
      {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
      {"name": "Vaquita", "habitat": "Marine", "population": 10}], "Vaquita"),
    ([{"name": "Kakapo", "habitat": "Forest", "population": 5},
      {"name": "Vaquita", "habitat": "Marine", "population": 5}], "Kakapo"),  # tie: lowest index wins
    ([{"name": "Vaquita", "habitat": "Marine", "population": 10}], "Vaquita"),
])
def test_prob01(species_list, expected):
    assert prob01(species_list) == expected
