from prob02 import reverse_comments_queue

def test_prob02():
    assert reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]) == ['Thanks for sharing.', 'Love it!', 'Great post!']
    assert reverse_comments_queue(["First!", "Interesting read.", "Well written."]) == ['Well written.', 'Interesting read.', 'First!']
