import pytest
from prob03 import prob03

CONTACTS = [
    ["Lupita Nyong'o", "Jordan Peele"],
    ["Meryl Streep", "Jordan Peele"],
    ["Meryl Streep", "Lupita Nyong'o"],
    ["Greta Gerwig", "Meryl Streep"],
    ["Ali Wong", "Greta Gerwig"],
]


@pytest.mark.parametrize("contacts, celeb, expected", [
    (CONTACTS, "Lupita Nyong'o", ['Jordan Peele', 'Meryl Streep']),   # example
    (CONTACTS, "Greta Gerwig", ['Ali Wong', 'Meryl Streep']),         # example
    (CONTACTS, "Ali Wong", ['Greta Gerwig']),                         # edge: one friend
    ([["A", "B"]], "B", ['A']),                                       # edge: single edge
])
def test_prob03(contacts, celeb, expected):
    assert sorted(prob03(contacts, celeb)) == expected
