import pytest
from prob02 import prob02

GET_OUT = {
    "Daniel Kaluuya": ["Allison Williams"],
    "Allison Williams": ["Daniel Kaluuya", "Catherine Keener", "Bradley Whitford"],
    "Bradley Whitford": ["Allison Williams", "Catherine Keener"],
    "Catherine Keener": ["Allison Williams", "Bradley Whitford"],
    "Jordan Peele": ["Jason Blum", "Gregory Plotkin", "Toby Oliver"],
    "Toby Oliver": ["Jordan Peele", "Gregory Plotkin"],
    "Gregory Plotkin": ["Jason Blum", "Toby Oliver", "Jordan Peele"],
    "Jason Blum": ["Jordan Peele", "Gregory Plotkin"],
}


def normalize(groups):
    # both the two lists and the names inside may come back in any order
    return sorted(sorted(g) for g in groups)


@pytest.mark.parametrize("graph, expected", [
    (GET_OUT, [["Daniel Kaluuya", "Allison Williams", "Catherine Keener", "Bradley Whitford"],
               ["Jordan Peele", "Jason Blum", "Gregory Plotkin", "Toby Oliver"]]),
    ({"A": [], "B": []}, [["A"], ["B"]]),
])
def test_prob02(graph, expected):
    assert normalize(prob02(graph)) == normalize(expected)
