# SETS — an unordered collection of UNIQUE items. No duplicates, no indexing.
# Use a set when you care about "is this present?" or "what's shared/different?"
# Membership tests (x in s) are O(1) average — much faster than a list's O(n).

empty_dict = {}      # NOTE: {} is an empty DICT, not a set — a common gotcha.
empty_set = set()    # the ONLY way to make an empty set.

# Duplicates collapse automatically. Also note 1 and "1" are DIFFERENT items
# (int vs str), so both survive; the repeated 1s and "1"s do not.
nums = {1, 2, 3, 1, 2, 3, 1, "1", 1, "1"}   # -> {1, 2, 3, "1"}
# nums.remove(5)   # remove() raises KeyError if the item is missing...
nums.discard(1)    # ...discard() removes if present, does nothing if not. Safer.
print(nums)

students_A = {"Alice", "Bob", "Carol"}
students_B = {"Bob", "Carol", ""}

# THE FOUR SET OPERATIONS — think of two overlapping circles (Venn diagram):
union = students_A | students_B      # everything in EITHER set
intersect = students_A & students_B  # only what's in BOTH
diffA = students_A - students_B      # in A but NOT in B
diffB = students_B - students_A      # in B but NOT in A (order matters for -)
sym = students_A ^ students_B        # in one OR the other, but NOT both (the non-overlap)

print(f'Intersection of students_A and students_B: {intersect}')
print(f'Union of students_A and students_B: {union}')
print(f'Difference of students_A and students_B: {diffA}')
print(f'Difference of students_B and students_A: {diffB}')
print(f'Symmetric Difference of students_A and students_B: {sym}')
