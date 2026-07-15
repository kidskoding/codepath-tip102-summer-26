import pytest
from prob02 import reverse_comments_queue

@pytest.mark.parametrize("comments, expected", [
    (["Great post!", "Love it!", "Thanks for sharing."], ['Thanks for sharing.', 'Love it!', 'Great post!']),
    (["First!", "Interesting read.", "Well written."], ['Well written.', 'Interesting read.', 'First!']),
    ([], []),              # empty queue
    (["only"], ["only"]),  # single element
])
def test_prob02(comments, expected):
    # reverse_comments_queue mutates its arg in place; pass a fresh copy per row
    assert reverse_comments_queue(list(comments)) == expected
