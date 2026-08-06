import pytest
from prob04 import prob04


def normalize(graph):
    return {k: sorted(v) for k, v in graph.items()}


@pytest.mark.parametrize("flights, expected", [
    (
        [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'],
         ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']],
        {
            'Cape Town': ['Addis Ababa', 'Cairo'],
            'Addis Ababa': ['Cape Town', 'Lagos'],
            'Lagos': ['Cairo', 'Addis Ababa'],
            'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
            'Nairobi': ['Cairo'],
        },
    ),                                                      # example
    ([], {}),                                               # edge: no flights
    ([['A', 'B']], {'A': ['B'], 'B': ['A']}),               # edge: single edge
])
def test_prob04(flights, expected):
    assert normalize(prob04(flights)) == normalize(expected)
