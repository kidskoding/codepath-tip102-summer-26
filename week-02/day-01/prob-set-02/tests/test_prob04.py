import pytest
from prob04 import prob04


@pytest.mark.parametrize("experiment1, experiment2, expected", [
    ({'temperature': 22, 'pressure': 101.3, 'humidity': 45},
     {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5},
     {'temperature': 22, 'humidity': 45}),
    ({'pressure': 101.3}, {'pressure': 101.3}, {}),
    ({}, {'pressure': 101.3}, {}),
])
def test_prob04(experiment1, experiment2, expected):
    assert prob04(experiment1, experiment2) == expected
