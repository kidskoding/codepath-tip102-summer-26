import pytest
from prob05 import prob05


# ties allow any top suggestion, so check membership in the set of winners
@pytest.mark.parametrize("votes, winners", [
    (["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"], {"Colbert"}),
    (["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"], {"Colbert", "Serenity"}),
    (["Tranquility"], {"Tranquility"}),
])
def test_prob05(votes, winners):
    assert prob05(votes) in winners
