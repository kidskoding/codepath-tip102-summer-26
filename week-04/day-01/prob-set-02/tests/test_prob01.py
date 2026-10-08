import pytest
from prob01 import prob01


@pytest.mark.parametrize("memes, max_length, expected", [
    (["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"],
     20, ["This is hilarious!", "Short and sweet"]),
    (["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"],
     15, ["Just right", "Perfect length"]),
    (["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"],
     10, ["Short", "Tiny meme"]),
    ([], 10, []),
])
def test_prob01(memes, max_length, expected):
    assert prob01(memes, max_length) == expected
