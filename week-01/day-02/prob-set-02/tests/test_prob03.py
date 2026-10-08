import pytest
from prob03 import prob03


@pytest.mark.parametrize("people, secret_identity, expected", [
    (['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne'], 'Bruce Wayne',
     ['Batman', 'Superman', 'The Riddler']),
    (['Batman', 'Robin'], 'Bruce Wayne', ['Batman', 'Robin']),
    (['Bruce Wayne', 'Bruce Wayne'], 'Bruce Wayne', []),
    ([], 'Bruce Wayne', []),
])
def test_prob03(people, secret_identity, expected):
    result = prob03(people, secret_identity)
    assert result == expected
    assert people == expected  # must modify the list in place
