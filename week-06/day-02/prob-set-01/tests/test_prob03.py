import pytest
from references import Node
from prob03 import prob03


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


@pytest.mark.parametrize("values, threshold, expected", [
    # 1 -> 4 -> 3 -> 2 -> 5 -> 2, threshold = 3  ->  4 -> 5 -> 1 -> 3 -> 2 -> 2
    ([1, 4, 3, 2, 5, 2], 3, [4, 5, 1, 3, 2, 2]),
    # empty list -> None
    ([], 3, None),
    # all values > threshold (order within group preserved by this impl)
    ([5, 6, 7], 3, [5, 6, 7]),
    # all values <= threshold (order within group preserved by this impl)
    ([1, 2, 3], 5, [1, 2, 3]),
])
def test_prob03(values, threshold, expected):
    result = prob03(build(values), threshold)
    assert (result if result is None else to_list(result)) == expected
