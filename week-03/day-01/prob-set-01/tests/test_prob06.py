import pytest
from prob06 import post_editor

@pytest.mark.parametrize("post, expected", [
    ("Boost your engagement with these tips", "tsooB ruoy tnemegegna htiw esehT spit"),
    ("Check out my latest vlog", "kcehC tuo ym tseval golv"),
])
def test_prob06(post, expected):
    assert post_editor(post) == expected
