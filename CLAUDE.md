# codepath-tip102-summer-26

CodePath TIP-102 Summer 2026 — weekly problem sets in Python.

## Project Structure

```
week-XX/
  day-XX/
    prob-set-XX/     # problem files: prob01.py, prob02.py, ...
    session-notes/   # scratch files and notes from class
  tests/
    day-XX/
      prob-set-XX/   # test files: test_prob03.py, conftest.py, ...
```

Directories use zero-padded numbers: `week-01`, `day-01`, `prob-set-01`.

## Running Tests

```bash
uv run pytest
```

Tests use `conftest.py` for dynamic path resolution — no manual `sys.path` needed.

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
