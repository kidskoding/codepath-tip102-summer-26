import pytest
from prob05 import prob05


# ties allow any top artist, so check membership in the set of winners
@pytest.mark.parametrize("votes, winners", [
    ({1234: "SZA", 1235: "Yo-Yo Ma", 1236: "Ethel Cain", 1237: "Ethel Cain", 1238: "SZA", 1239: "SZA"},
     {"SZA"}),
    ({1234: "SZA", 1235: "Yo-Yo Ma", 1236: "Ethel Cain", 1237: "Ethel Cain", 1238: "SZA"},
     {"SZA", "Ethel Cain"}),
    ({1234: "Yo-Yo Ma"}, {"Yo-Yo Ma"}),
])
def test_prob05(votes, winners):
    assert prob05(votes) in winners
