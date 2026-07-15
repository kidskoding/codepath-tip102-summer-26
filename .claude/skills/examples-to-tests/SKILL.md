---
name: examples-to-tests
description: Use when asked to turn a problem set's examples into pytest tests, generate test files, or "write tests for these problems". Reads the Input/Output examples from a prob-set's problem-set.md and writes test_probNN.py files into a tests/ folder inside that prob-set (week-XX/day-XX/prob-set-XX/tests/), one per problem. Triggers on "make tests", "turn examples into tests", "generate test files", "test_probNN".
---

# Examples → Tests

## Overview

Turn the worked examples in a problem set into runnable pytest files, one `test_probNN.py` per problem, placed in the mirrored `tests/` tree. Mechanically follows the existing week-01 convention — don't invent a new layout.

## Cover EVERY problem (do this first)

Enumerate every `## Problem N` heading in `problem-set.md`. Produce one test per
problem, NOT one per existing `probNN.py` — a problem with no solution file yet
still gets a test.

**Skip a problem (write NO test) when there's nothing meaningful to assert:**
- a debugging/review/"fix this code" problem with no function signature, OR
- a **print-only** problem — the function just `print`s and returns `None`, with
  no return value and no object state to inspect. Do NOT use `capsys` /
  stdout-capture to test these. If the only "output" is a printed string, skip
  the problem entirely — a print statement isn't worth a test.

Everything else (a real return value, or observable object/list state after the
call) gets a faithful test.

For each problem `N` with no `probNN.py`, first create the stub so its test can
import and skip:
```python
# probNN.py
from references import Node  # only if the signature uses Node

def probNN(...):
    pass
```
Then write `test_probNN.py` for it like any other. Result: a set with 6 problems
and 2 solutions yields 6 test files — 2 pass, 4 skip. Never stop at the count of
existing solution files.

## Where tests go

Tests live in a `tests/` folder INSIDE each prob-set, next to the problems:
```
week-XX/day-XX/prob-set-XX/
  probNN.py
  tests/
    conftest.py        # required — makes imports work
    test_probNN.py
```
`probNN` ↔ `test_probNN` (zero-padded, matching the source file). Run a whole
set with one path: `uv run pytest week-XX/day-XX/prob-set-XX`.

## conftest.py (copy verbatim)

Every `tests/` folder needs this `conftest.py`. It (1) puts the PARENT prob-set
dir on `sys.path` so `from probNN import probNN` resolves, and (2) turns an
unwritten stub into a **skip** instead of a failure. Create it if missing; copy
verbatim, never edit:

```python
import ast
import sys
from pathlib import Path

import pytest

PROB_SET = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROB_SET))


def _is_stub(fn):
    """True if fn's body is just `pass` (ignoring a docstring)."""
    body = [
        n
        for n in fn.body
        if not (
            isinstance(n, ast.Expr)
            and isinstance(n.value, ast.Constant)
            and isinstance(n.value.value, str)
        )
    ]
    return len(body) == 1 and isinstance(body[0], ast.Pass)


def pytest_runtest_setup(item):
    # test_probNN.py -> probNN.py; an unwritten `pass` stub skips, not fails.
    src = PROB_SET / f"{item.path.stem.removeprefix('test_')}.py"
    if not src.exists():
        return
    fns = [
        n
        for n in ast.walk(ast.parse(src.read_text()))
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    if any(_is_stub(fn) for fn in fns):
        pytest.skip("not implemented")
```

Unwritten stubs are `pass` (never `raise NotImplementedError`) — the conftest reads
the source and skips as soon as any function in `probNN.py` is still a bare `pass`.
That covers class problems too, where `__init__` is given but the method under test
is a stub. Once every function has a real body, the tests run. Never touch a stub
that already has a real solution.

## test_probNN.py template

Use `@pytest.mark.parametrize` with one row per case — the given examples PLUS
the obvious edge cases. Each case runs and is reported independently, so one
failing case doesn't mask the others (stacked `assert`s stop at the first
failure — don't use them for multiple cases):

```python
import pytest
from probNN import probNN

@pytest.mark.parametrize("arg, expected", [
    (input1, expected1),   # example from problem-set.md
    (input2, expected2),   # example from problem-set.md
    (empty,  expected_e),  # edge case (see below), answer computed by hand
    (single, expected_s),  # edge case
])
def test_probNN(arg, expected):
    assert probNN(arg) == expected
```

For a multi-arg signature, widen the param string and unpack:
```python
@pytest.mark.parametrize("a, b, expected", [
    (input_a, input_b, expected1),
])
def test_probNN(a, b, expected):
    assert probNN(a, b) == expected
```

Rules:
- Import `probNN` from `probNN` — the function is named after the problem number, not
  whatever the problem text calls it (see `format-problem-set`). Exceptions: class-def
  problems (methods keep their names) and two-function problems (both keep theirs).
- One parametrize row per Input/Output example in `problem-set.md`, using the real values, not paraphrases — then add the edge-case rows below.
- Test function is named `test_probNN` matching the file.
- `parametrize` is the one pytest feature to use here (for per-case failure isolation). Still no other fixtures and no speculative test scaffolding.

### Add the obvious edge cases (don't stop at the given example)

A single example passing hides bugs — a linked-list solution that "works" can
still crash on a single node or drop a final carry. Beyond the stated examples,
add the edge cases that are **obvious and unambiguous for that problem shape** —
ones where you can compute the correct answer by hand with certainty. Only add a
case when you're sure of its expected value; never invent an input whose output
you'd have to guess.

Common ones by shape:
- **Any list/collection input** → empty input (`[]` / `None`) and a single-element input.
- **Linked-list rotate / shift / partition by `k`** → `k = 0`, `k` larger than the list length (wrap-around), and a single-node list.
- **Add / sum of digits or numbers** → a case whose final step carries (e.g. `5 + 5`, `99 + 1`) so the trailing carry node is exercised.
- **Cycle / two-pointer** → no-cycle, whole-list cycle, and single node.
- **Search / index** → target absent (returns -1 / None), first element, last element.
- **String/number transforms** → empty string / `0`, and a value that stays the same after the transform.

Pick the 1–3 that actually apply to the problem; skip ones that don't fit. If
the function's edge behavior is genuinely ambiguous from the spec (not clearly
defined), leave that case out rather than assert a guessed value.

## Linked lists (and other object inputs)

When examples use a `Node`/linked list, the raw `print(func(...))` won't translate to `==` directly. Two helpers make it work — define them at the top of the test file:

```python
from references import Node        # shared class, repo-root references package
from prob04 import prob04  # the solution under test

def build(values):
    """list -> linked list, returns head"""
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head

def to_list(head):
    """linked list -> list, for comparison"""
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out

@pytest.mark.parametrize("a_vals, b_vals, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),  # example
    ([],        [1],       [1]),                  # one empty
    ([],        [],        []),                   # both empty
])
def test_prob04(a_vals, b_vals, expected):
    assert to_list(prob04(build(a_vals), build(b_vals))) == expected
```

- Pass plain lists in the parametrize rows and call `build()` inside the test
  body — keeps the rows readable and rebuilds fresh nodes per case.
- Import `Node` from `references` (`from references import Node`) — the shared
  class every solution uses. `conftest.py` puts the repo root on `sys.path`, and
  its attribute is `.value` (not `.val`).
- Compare on the list form (`to_list`) or a boolean the function returns — never on Node objects directly unless the function returns a bool.
- For a `bool`-returning problem (e.g. `is_circular`), the structure (esp. a
  cycle) can't be expressed as a plain list — build it by hand in the test body
  and assert `== True`/`== False`. A plain `def test_probNN()` is fine here
  instead of parametrize when each case needs custom wiring.

## After writing

Run and confirm implemented ones pass and unwritten ones **skip**:
```bash
uv run pytest week-XX/day-XX/prob-set-XX -q
```
Expected output shape: `N passed, M skipped`. A `skipped` test = its `probNN.py` is
still a bare `pass` stub — that's correct, the solution just isn't written yet. You
should see NO failures. A failure means either a wrong expected value in the test or
a real solution bug — never "fix" it by weakening the test.

## Don't

- Don't skip `conftest.py` — imports break without it.
- Don't add speculative test cases beyond the stated examples.
- Don't redefine `Node` in the test; import it from the solution.
