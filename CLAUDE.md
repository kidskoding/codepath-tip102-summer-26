# codepath-tip102-summer-26

CodePath TIP-102 Summer 2026 — weekly problem sets in Python.

## Project Structure

```
references/              # central shared classes: Node, Villager, Player, ...
week-XX/
  day-XX/
    prob-set-XX/         # problem files: prob01.py, prob02.py, ...
      tests/             # test files: test_prob01.py, conftest.py
    session-notes/       # scratch files and notes from class
```

Directories use zero-padded numbers: `week-01`, `day-01`, `prob-set-01`.

## Running Tests

Tests live in a `tests/` folder INSIDE each prob-set. Run one set with one path:

```bash
uv run pytest week-05/day-01/prob-set-01
```

Run tests per prob-set, NOT the whole repo — `uv run pytest` at the root
collides on duplicate `test_probNN.py` module names across sets.
Each `tests/` has a `conftest.py` that puts the parent prob-set dir on `sys.path`,
so tests import `from probNN import probNN` (and `from references import Node`) with
no manual path setup. That conftest also reports unwritten solutions as **skipped**:
it reads `probNN.py` and skips the test while any function there is still a bare
`pass`. Solutions stub with `pass`, never `raise NotImplementedError`. A test that
fails (rather than skips) is a real failure — don't weaken the test to pass.

Shared classes (`Node`, `Villager`, `Player`, …) live in one central repo-root
`references/` package, each defined once as the superset version and imported via
`from references import ...`. `pyproject.toml` puts the repo root on `sys.path`
(`pythonpath = ["."]`) so the import resolves from any set.

## Python Version

Managed by `uv`. Version pinned in `.python-version`. Run `uv python pin X.Y` to change.

## Problem Set Markdown

Each `prob-set-XX/` has a `problem-set.md` with the full problem descriptions. No hints included.

## Key Rules

- Always use `uv run` — not `python` directly
- Zero-padded directory names only (`week-01` not `week-1`)
- One function per `probXX.py` file matching the problem signature exactly
- Skip `probXX.py` for debugging/review problems (no implementation file needed); delete if one already exists
- When a week has two problem set versions, use separate `prob-set-01/` (v1) and `prob-set-02/` (v2) directories, each with its own `problem-set.md`
