from prob02 import prob02, Node


def test_prob02():
    # clue1 -> clue2 -> clue3 -> clue4 -> clue2  (4th points to 2nd)
    clue1 = Node('clue1')
    clue2 = Node('The stolen goods are at an abandoned warehouse')
    clue3 = Node('The mayor is accepting bribes')
    clue4 = Node('They dumped their disguise in the lake')
    clue1.next = clue2
    clue2.next = clue3
    clue3.next = clue4
    clue4.next = clue2
    assert sorted(prob02(clue1)) == sorted([
        'The stolen goods are at an abandoned warehouse',
        'The mayor is accepting bribes',
        'They dumped their disguise in the lake',
    ])

    # clue5 -> clue6 -> clue7  (no cycle)
    clue5 = Node('clue5')
    clue6 = Node('clue6')
    clue7 = Node('clue7')
    clue5.next = clue6
    clue6.next = clue7
    assert prob02(clue5) == []

    # whole-list cycle: 1 -> 2 -> 3 -> 1  (every value is in the cycle)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3
    n3.next = n1
    assert sorted(prob02(n1)) == [1, 2, 3]
