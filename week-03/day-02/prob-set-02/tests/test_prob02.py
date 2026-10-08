import pytest
from prob02 import prob02


@pytest.mark.parametrize("landmarks, expected", [
    (["canyon", "forest", "rotor", "mountain"], "rotor"),
    (["plateau", "valley", "cliff"], ""),
    ([], ""),
    (["level", "rotor"], "level"),
])
def test_prob02(landmarks, expected):
    assert prob02(landmarks) == expected
