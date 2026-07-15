import pytest
from prob07 import prob07


@pytest.mark.parametrize("actions, expected", [
    (["add", "add", "remove", "remove"], True),
    (["add", "remove", "add", "remove"], True),
    (["add", "remove", "remove", "add"], False),
    # edge: remove before any add (from the problem set's trailing note)
    (["remove", "add"], False),
    # edge: unclosed add / lone remove
    (["add"], False),
    (["remove"], False),
    # edge: empty sequence is trivially balanced
    ([], True),
])
def test_prob07(actions, expected):
    assert prob07(actions) == expected
