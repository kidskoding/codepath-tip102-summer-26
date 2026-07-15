# Happy Number
# Source - https://leetcode.com/problems/happy-number/description/

# Time:  O(log n) - each step processes the digits of n (log10(n) of them). After
#                   the first step values drop below ~243 and cycle within a bounded
#                   range, so the number of steps is constant; the log n first pass dominates.
# Space: O(log n) - the set holds the values visited before repeating, bounded by the
#                   same small reachable range plus the initial n.
def demo_problem(n: int) -> bool:
    st = set()
    while n != 1 and n not in st:
        st.add(n)

        n_str = str(n)
        total = 0
        for c in n_str:
            total += int(c) ** 2

        n = total

    return n == 1
