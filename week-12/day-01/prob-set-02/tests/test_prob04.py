import pytest
from prob04 import prob04


def is_subsequence(chosen, pokemon):
    it = iter(pokemon)
    return all(name in it for name in chosen)


@pytest.mark.parametrize("pokemon, types, best_length", [
    (["Pikachu", "Bulbasaur", "Charmander"], [0, 0, 1], 2),
    (["Squirtle", "Pidgey", "Rattata", "Gengar"], [1, 0, 1, 1], 3),
    (["Pikachu"], [0], 1),
    (["Pikachu", "Bulbasaur", "Charmander"], [1, 1, 1], 1),  # all the same type
    (["A", "B", "C", "D"], [0, 1, 0, 1], 4),  # already alternating
])
def test_prob04(pokemon, types, best_length):
    # any longest alternating subsequence is accepted, so check its properties
    team = prob04(pokemon, types)
    type_of = dict(zip(pokemon, types))
    assert len(team) == best_length
    assert is_subsequence(team, pokemon)
    assert all(type_of[a] != type_of[b] for a, b in zip(team, team[1:]))
