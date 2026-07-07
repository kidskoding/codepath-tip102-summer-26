# ============================================================================
# RECURSION — a function that calls itself on a SMALLER version of the problem.
# Every recursion has two parts:
#   1. BASE CASE      — the smallest input, answered directly. Stops recursion.
#   2. RECURSIVE CASE — do a little work, then call yourself on something smaller.
# The magic: you TRUST the recursive call to return the right answer, and just
# combine it. Each call must move CLOSER to the base case, or it never stops.
# ============================================================================


# --- factorial: n! = n * (n-1) * ... * 1 -----------------------------------
def factorial(n):
    if n == 0:            # BASE CASE: 0! = 1 by definition. The stopping point.
        return 1
    else:
        return n * factorial(n-1)   # do work (n *), recurse on smaller (n-1).
        # Trace factorial(3):
        #   3 * factorial(2)
        #   3 * (2 * factorial(1))
        #   3 * (2 * (1 * factorial(0)))
        #   3 * (2 * (1 * 1))  =  6
        # Notice: nothing multiplies until the base case returns, then it
        # "unwinds" back up, multiplying on the way out.
print(factorial(5))


# --- fibonacci: each number is the sum of the previous two ------------------
def fibonacci(n):
    if n == 0:            # BASE CASE 1
        return 0
    elif n == 1:          # BASE CASE 2 — here we need TWO base cases, because the
        return 1          # recursive step reaches back TWO steps (n-1 and n-2).
    return fibonacci(n-1) + fibonacci(n-2)   # combine two smaller subproblems.
print(fibonacci(10))
# CONCEPT — branching recursion: this makes TWO calls, so the calls form a
# TREE, not a straight line. That tree recomputes the same values repeatedly
# (fib(2) is calculated many times), which is why naive fibonacci is slow:
# roughly O(2^n). Same subproblem solved over and over = a signal that caching
# (memoization) would help. Understand the waste first; optimize second.


# --- reverse_string: recursion works on strings/lists too, not just numbers -
def reverse_string(s):
    if len(s) <= 1:       # BASE CASE: a string of 0 or 1 char is its own reverse.
        return s
    rest = s[:-1]         # THE SMALLER PROBLEM: the string without its last char.
    print(rest)           # (watch it shrink each call — a learning aid, not needed)
    return s[-1] + reverse_string(rest)   # put last char first, then reverse rest.
    # Trace "cat":
    #   'c'..'a'..'t'  ->  't' + reverse("ca")
    #                   ->  't' + ('a' + reverse("c"))
    #                   ->  't' + ('a' + 'c')  =  "tac"
print(reverse_string("apple"))


# --- list_length: recursion over a LINKED LIST -----------------------------
def list_length(node):
    if node is None:      # BASE CASE: reached the end of the list (no node).
        return 0
    return 1 + list_length(node.next)   # count THIS node + length of the rest.
    # SAME SHAPE as factorial: "1 + (smaller problem)". Once you see the pattern —
    # base case + combine-with-smaller — it transfers across data structures.
    # (No call to run this one: it needs an actual linked list of Nodes to walk.)


# --- test: notice this is factorial again, under a different name -----------
def test(n):
    if n == 0:
        return 1
    return n * test(n-1)
print(test(5))
# Recognizing that two functions share the SAME recursive shape (base case +
# n * smaller) is exactly the skill to build. The pattern matters more than
# the name on the function.

# ============================================================================
# THE ONE THING TO REMEMBER:
#   base case (stop)  +  recursive case (smaller problem, then combine).
# If you can name those two parts for any recursion, you understand it.
# ============================================================================
