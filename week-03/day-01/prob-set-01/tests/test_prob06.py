import pytest
from prob06 import prob06

@pytest.mark.parametrize("post, expected", [
    ("Boost your engagement with these tips", "tsooB ruoy tnemegegna htiw esehT spit"),
    ("Check out my latest vlog", "kcehC tuo ym tseval golv"),
])
def test_prob06(post, expected):
    assert prob06(post) == expected
