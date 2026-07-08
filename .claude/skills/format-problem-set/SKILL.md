---
name: format-problem-set
description: Use when given raw copy-pasted problem set text (from CodePath, LeetCode, HackerRank, etc.) and asked to create a structured markdown file. Triggers on phrases like "make a problem set", "format this into markdown", "create a problem file", or when raw problem text is pasted alongside a request to save/format it.
---

# Format Problem Set

## Overview

Convert raw copy-pasted problem text into a clean, structured markdown file formatted like a HackerRank/CodePath problem set. One problem per `##` section, consistent structure throughout.

## Output File Location

Save to the most relevant path in the project. Default:
```
week-XX/day-XX/prob-set-XX/problem-set.md
```
Ask user if path is unclear.

## Markdown Template

```markdown
# Problem Set: [Topic] — Week X, Day X

---

## Problem N: [Title]

**Difficulty:** Easy / Medium / Hard

### Description

[Problem description written in second-person, present tense. Clean prose, no raw formatting artifacts from the source.]

**A solution is considered valid if:**
- Condition 1
- Condition 2

### Function Signature

```python
def function_name(param: type) -> return_type:
    pass
```

### Examples

**Example 1:**
```
Input:  ...
Output: ...
```

**Example 2:**
```
Input:  ...
Output: ...
```

### Constraints

- Constraint 1 (if stated)

---
```

## Also create probNN.py stub files

After writing `problem-set.md`, create one `probNN.py` solution stub per problem
in the SAME `prob-set-XX/` dir (zero-padded, matching the problem number):

```
week-XX/day-XX/prob-set-XX/
  problem-set.md
  prob01.py
  prob02.py
  ...
```

Each stub holds only the exact function signature from that problem, with a
`raise NotImplementedError` body (NOT `pass`) — plus any class (e.g. `Node`) the
signature depends on. Raising (instead of `pass`) lets the test conftest report
unwritten solutions as **skipped** rather than failed:

```python
# prob03.py
def partition(suspect_ratings, threshold):
    raise NotImplementedError
```

Rules for stubs:
- **Check the dir first (`ls`). If a `probNN.py` already exists, NEVER touch it** —
  not the stub, not a rewrite, nothing. Skip every problem number already present,
  whether the file has real code, a `pass` stub, or is empty. Only create stubs for
  problem numbers with NO existing file.
- One file per problem, `probNN` matching the `## Problem N` number.
- **The FILE is always named `probNN.py` by problem number — ignore what the problem
  calls the function.** "Write a function `welcome()`" → file `prob01.py`, NOT
  `welcome.py`. The function name only lives inside the file as the signature.
- Copy the signature EXACTLY as given (same name, params, type hints). Don't invent one.
- **Skip debug/review problems** — if a problem has no function to implement (it's
  "find the bug" / "trace this code"), don't create a `probNN.py` for it (per CLAUDE.md).
- **Shared classes go in a per-set `references/` package, NOT copied into each stub.**
  If problems in the set share a class (`Node`, `Villager`, `Player`, …), create
  `prob-set-XX/references/` with one file per class plus an `__init__.py` that
  re-exports them, then have stubs and tests do `from references import Node`. The
  per-set `tests/conftest.py` puts the prob-set dir on `sys.path`, so this resolves
  to the LOCAL package (not any other week's). See the "Per-set references" section.

## Per-set references

When a set's problems share a class, it lives ONCE in a `references/` package
inside that prob-set — each set is self-contained, no repo-root shared module:

```
week-XX/day-XX/prob-set-XX/
  references/
    __init__.py      # from .node import Node ; __all__ = ["Node"]
    node.py          # class Node: ...
  prob01.py          # from references import Node
  tests/
    test_prob01.py   # from references import Node
```

- One file per class (`node.py`, `villager.py`, `player.py`), `__init__.py` re-exports.
- If the class evolves across the set (later problems add a field), define the
  **superset** version in `references/` so every problem's usage works.
- Stubs/tests import the class with `from references import ClassName` — NOT from
  a `probNN` module, and NOT a copy pasted into each file.
- Class-DEFINITION problems (the exercise is "write the class with method X") keep
  their own class in `probNN.py` — those aren't shared, they're the assignment.
- Because every set names its package `references`, RUN TESTS PER SET (the module
  name collides if two sets are collected in one `pytest` invocation).

## Then generate the tests

After `problem-set.md` and the stubs are written, ALWAYS chain into the
`examples-to-tests` skill for the same prob-set(s) — invoke it via the Skill
tool (`skill: "examples-to-tests"`) with the prob-set path(s) as args. That
skill reads the examples you just wrote and produces `tests/` + `test_probNN.py`.
Do this automatically; don't wait for the user to ask. Skip only if the user
explicitly said "no tests" / "just the markdown".

## Rules

1. **Strip noise** — remove emoji, hints, raw `print()` calls used as examples, duplicate blank lines, broken formatting from copy-paste
2. **No hints section** — drop all `💡 Hint` and `✨ AI Hint` content entirely
3. **Normalize examples** — convert `print(func(args))` → `Output: result` format
4. **One file, all problems** — don't split into separate files unless user asks
5. **Infer difficulty** if not stated — Easy for direct lookups, Medium for two-pointer/stack, Hard for complex logic
6. **Keep function signature** exactly as given — don't rename params or change types
7. **Starter code** — if a problem asks to "add comments to existing code", include the full code block under a `### Starter Code` section

## Common Mistakes

- Leaving raw `print(func(...))` calls instead of formatting as Input/Output examples
- Including hints — drop them always
- Forgetting the `---` horizontal rule between problems
- Writing file to wrong week/day directory — confirm with user if unsure
