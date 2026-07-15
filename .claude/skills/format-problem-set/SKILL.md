---
name: format-problem-set
description: Use when given raw copy-pasted problem set text (from CodePath, LeetCode, HackerRank, etc.) and asked to create a structured markdown file. Triggers on phrases like "make a problem set", "format this into markdown", "create a problem file", or when raw problem text is pasted alongside a request to save/format it.
---

# Format Problem Set

## Overview

Convert raw copy-pasted problem text into a clean, structured markdown file formatted like a HackerRank/CodePath problem set. One problem per `##` section, consistent structure throughout.

## Non-algorithmic problems → mark (SKIPPED), no stub

If a problem is NOT an algorithmic implementation problem — i.e. there is no
function for the student to write — it gets SKIPPED. This covers discuss/compare
problems ("compare your solution to the one below", "which do you prefer?",
"discuss with your podmates"), debug/review/trace problems, and any prompt whose
"answer" is prose rather than code.

For a skipped problem:
- In `problem-set.md`, title it `## Problem N: [Title] (SKIPPED)` and keep a short
  Description so the numbering stays intact, but DO NOT add a Function Signature,
  Examples, or Constraints section. A one-line note like
  `_Discussion/comparison problem — no implementation._` is enough.
- Create NO `probNN.py` stub for it.
- The `examples-to-tests` step also skips it (no signature = no test).

A problem that DOES have a function to implement but also asks a discussion
question (e.g. "implement X, then discuss the tradeoffs") is NOT skipped — format
it normally; the discussion prompt is just dropped.

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
def probNN(param: type) -> return_type:
    pass
```

**Always name the function `probNN` (matching the problem number), even when the
problem says "write a function `foo()`".** Keep the params and type hints exactly
as given — only the name is overridden.

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
def prob03(suspect_ratings, threshold):
    raise NotImplementedError
```

Rules for stubs:
- **Check the dir first (`ls`). If a `probNN.py` already exists, NEVER touch it** —
  not the stub, not a rewrite, nothing. Skip every problem number already present,
  whether the file has real code, a `pass` stub, or is empty. Only create stubs for
  problem numbers with NO existing file.
- One file per problem, `probNN` matching the `## Problem N` number.
- **Both the FILE and the FUNCTION are named `probNN` by problem number — ignore what
  the problem calls the function.** "Write a function `welcome(name)`" → file
  `prob01.py` holding `def prob01(name):`. Not `welcome.py`, not `def welcome`.
- Copy the params and type hints EXACTLY as given; only the function name is
  overridden to `probNN`. Don't invent params.
- **Two exceptions to the `probNN` name.** (1) Class-DEFINITION problems: methods keep
  their given names (`def set_catchphrase(self, ...)`) — `probNN` names a module-level
  function, not a method. (2) A problem asking for TWO functions (e.g. "write it
  iteratively AND recursively") keeps both given names — they can't both be `probNN`.
- **Skip debug/review problems** — if a problem has no function to implement (it's
  "find the bug" / "trace this code"), don't create a `probNN.py` for it (per CLAUDE.md).
- **Shared classes go in the central repo-root `references/` package, NOT copied
  into each stub.** If problems share a class (`Node`, `Villager`, `Player`, …),
  add it to `references/` and have stubs and tests do `from references import Node`.
  See the "Central references" section.

## Central references

Shared classes live ONCE in a single repo-root `references/` package. Every set
imports from it; `pyproject.toml` has `pythonpath = ["."]` so it resolves anywhere:

```
references/
  __init__.py        # from .node import Node ; ... ; __all__ = ["Node", ...]
  node.py            # class Node: ...
  villager.py        # class Villager: ...
week-XX/day-XX/prob-set-XX/
  prob01.py          # from references import Node
  tests/
    test_prob01.py   # from references import Node
```

- One file per class (`node.py`, `villager.py`, `player.py`), `__init__.py` re-exports.
- If a class evolves across a set (later problems add a field), define the
  **superset** version so every problem's usage works.
- Stubs/tests import with `from references import ClassName` — NOT from a `probNN`
  module, and NOT a copy pasted into each file.
- Class-DEFINITION problems (the exercise is "write the class with method X") keep
  their own class in `probNN.py` — those aren't shared, they're the assignment.
- Give each class a distinct name across the whole repo (one `Node`, one `Villager`)
  since they now share a namespace.

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
6. **Keep params and types** exactly as given — don't rename params or change types.
   The function NAME is always `probNN`, whatever the problem calls it.
7. **Starter code** — if a problem asks to "add comments to existing code", include the full code block under a `### Starter Code` section

## Common Mistakes

- Leaving raw `print(func(...))` calls instead of formatting as Input/Output examples
- Including hints — drop them always
- Forgetting the `---` horizontal rule between problems
- Writing file to wrong week/day directory — confirm with user if unsure
