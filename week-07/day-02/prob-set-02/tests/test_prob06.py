import pytest
from prob06 import merge_sort_playlist


@pytest.mark.parametrize("playlist, expected", [
    (["Formation", "Crazy in Love", "Halo"], ["Crazy in Love", "Formation", "Halo"]),
    (["Single Ladies", "Love on Top", "Irreplaceable"], ["Irreplaceable", "Love on Top", "Single Ladies"]),
    ([], []),
    (["Halo"], ["Halo"]),
])
def test_prob06(playlist, expected):
    assert merge_sort_playlist(playlist) == expected
