---
name: examples-to-tests
description: Use when asked to turn a problem set's examples into pytest tests, generate test files, or "write tests for these problems". Reads the Input/Output examples from a prob-set's problem-set.md and writes test_probNN.py files into a tests/ folder inside that prob-set (week-XX/day-XX/prob-set-XX/tests/), one per problem. Triggers on "make tests", "turn examples into tests", "generate test files", "test_probNN".
---

# Examples → Tests

## Overview

Turn the worked examples in a problem set into runnable pytest files, one `test_probNN.py` per problem, placed in the mirrored `tests/` tree. Mechanically follows the existing week-01 convention — don't invent a new layout.

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
dir on `sys.path` so `from probNN import fn` resolves, and (2) turns an
unimplemented stub (`raise NotImplementedError`) into a **skip** instead of a
failure. Create it if missing; copy verbatim, never edit:

```python
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def pytest_runtest_call(item):
    # Unimplemented stubs raise NotImplementedError -> report as skipped, not failed.
    try:
        item.runtest()
    except NotImplementedError:
        pytest.skip("not implemented")
```

For this to work, unwritten stubs must `raise NotImplementedError` (not `pass`).
If a `probNN.py` under test is still `pass`, change its body to
`raise NotImplementedError` so its test **skips** rather than fails on a `None`
return. Never touch a stub that already has a real solution.

## test_probNN.py template

One import, one `test_probNN()` function, one `assert` per example:

```python
from probNN import function_name

def test_probNN():
    assert function_name(input1) == expected1
    assert function_name(input2) == expected2
```

Rules:
- Import the exact function name from the problem's signature.
- One assert per Input/Output example in `problem-set.md`. Use the real values from the examples, not paraphrases.
- Test function is named `test_probNN` matching the file.
- No pytest fixtures, no parametrize, no extra edge cases the examples don't state — keep it a faithful transcription of the given examples. (Add an obvious edge case like empty input only if the problem's examples include it.)

## Linked lists (and other object inputs)

When examples use a `Node`/linked list, the raw `print(func(...))` won't translate to `==` directly. Two helpers make it work — define them at the top of the test file:

```python
from prob04 import Node, merge_timelines   # import Node from the SAME solution file

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

def test_prob04():
    a = build([1, 2, 4])
    b = build([1, 3, 4])
    assert to_list(merge_timelines(a, b)) == [1, 1, 2, 3, 4, 4]
```

- Import `Node` from the solution file, don't redefine it (identity comparisons must match).
- Compare on the list form (`to_list`) or a boolean the function returns — never on Node objects directly unless the function returns a bool.
- For a `bool`-returning problem (e.g. `is_circular`), build the structure by hand (including the cycle) and assert `== True`/`== False`.

## After writing

Run and confirm implemented ones pass and unwritten ones **skip**:
```bash
uv run pytest week-XX/day-XX/prob-set-XX -q
```
Expected output shape: `N passed, M skipped`. A `skipped` test = its `probNN.py`
still raises `NotImplementedError` — that's correct, the solution just isn't
written yet. You should see NO failures. A failure means either a wrong
expected value in the test or a real solution bug — never "fix" it by weakening
the test.

## Don't

- Don't skip `conftest.py` — imports break without it.
- Don't add speculative test cases beyond the stated examples.
- Don't redefine `Node` in the test; import it from the solution.
