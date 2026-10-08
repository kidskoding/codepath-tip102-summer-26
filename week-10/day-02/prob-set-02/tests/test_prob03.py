import pytest
from prob03 import prob03

BACON = {
    "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon", "Tom Cruise"],
    "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
    "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
    "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
    "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
    "George Clooney": ["Julia Roberts", "Vera Farmiga"],
    "Vera Farmiga": ["George Clooney", "Max Theriot"],
    "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
    "Jennifer Lawrence": ["Max Theriot"],
}


@pytest.mark.parametrize("network, celeb, expected", [
    (BACON, "Jennifer Lawrence", 5),
    (BACON, "Tom Cruise", 1),
    (BACON, "Kevin Bacon", 0),
    (BACON, "Denzel Washington", 2),  # shortest route, not the first one found
    ({**BACON, "Zendaya": []}, "Zendaya", -1),  # not connected
])
def test_prob03(network, celeb, expected):
    assert prob03(network, celeb) == expected
