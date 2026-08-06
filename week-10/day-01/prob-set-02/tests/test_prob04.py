import pytest
from prob04 import prob04

CLIENTS = [
    ["Yalitza Aparicio", "Julio Torres"],
    ["Julio Torres", "Fred Armisen"],
    ["Bowen Yang", "Julio Torres"],
    ["Bowen Yang", "Margaret Cho"],
    ["Margaret Cho", "Ali Wong"],
    ["Ali Wong", "Fred Armisen"],
    ["Ali Wong", "Bowen Yang"],
]


@pytest.mark.parametrize("clients", [
    CLIENTS,                # example
    [["A", "B"]],           # edge: single pair
])
def test_prob04(clients):
    # ID assignment order is up to the solution, so check the mapping and the
    # matrix are self-consistent with the given edges rather than fixing an order.
    names = {name for pair in clients for name in pair}
    id_map, matrix = prob04(clients)

    assert set(id_map.keys()) == names
    assert sorted(id_map.values()) == list(range(len(names)))
    assert len(matrix) == len(names)
    assert all(len(row) == len(names) for row in matrix)

    by_id = {i: name for name, i in id_map.items()}
    edges = {
        frozenset((by_id[i], by_id[j]))
        for i in range(len(names))
        for j in range(len(names))
        if matrix[i][j] == 1
    }
    assert edges == {frozenset(pair) for pair in clients}
