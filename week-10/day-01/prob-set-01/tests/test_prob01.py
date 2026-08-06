from prob01 import prob01

EXPECTED = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["ATL", "JFK"],
    "ATL": ["DFW"],
}


def normalize(graph):
    return {k: sorted(v) for k, v in graph.items()}


def test_prob01():
    assert normalize(prob01()) == normalize(EXPECTED)
