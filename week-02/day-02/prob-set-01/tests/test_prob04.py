import pytest
from prob04 import prob04


@pytest.mark.parametrize("observed_species, priority_species, expected", [
    (["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"], ["🐯", "🦌", "🐘", "🦁"],
     ["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐍", "🐻", "🐼", "🦑"]),
    (["bluejay", "sparrow", "cardinal", "robin", "crow"], ["cardinal", "sparrow", "bluejay"],
     ["cardinal", "sparrow", "bluejay", "crow", "robin"]),
    (["robin", "crow"], [], ["crow", "robin"]),
    ([], [], []),
])
def test_prob04(observed_species, priority_species, expected):
    assert prob04(observed_species, priority_species) == expected
