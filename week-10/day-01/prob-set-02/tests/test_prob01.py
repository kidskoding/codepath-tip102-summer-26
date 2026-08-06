from prob01 import prob01

EXPECTED = {
    "Kevin Bacon": ["Laverne Cox", "Sofia Vergara"],
    "Meryl Streep": ["Idris Elba", "Sofia Vergara"],
    "Idris Elba": ["Meryl Streep", "Laverne Cox"],
    "Laverne Cox": ["Kevin Bacon", "Idris Elba"],
    "Sofia Vergara": ["Kevin Bacon", "Meryl Streep"],
}


def normalize(graph):
    return {k: sorted(v) for k, v in graph.items()}


def test_prob01():
    assert normalize(prob01()) == normalize(EXPECTED)
