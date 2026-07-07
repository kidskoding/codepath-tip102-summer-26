---
name: teach-notes
description: Use when asked to add teaching notes, explain code with comments, or annotate a file "like an instructor/teacher would". Adds inline comments to existing code that TEACH the underlying concepts (how it works, why, the pattern, the trace) — for study and review. Triggers on "make notes on this code", "teach notes", "explain this as comments", "annotate like a teacher", "add teaching comments".
---

# Teach Notes

## Overview

Annotate existing code with **teaching comments** — the kind a good instructor writes in the margin to help a student *learn the concept*, not to grade the code. Edit the file in place, adding comments; do not rewrite the logic.

Goal: after reading the annotated file, the student understands HOW it works, WHY it's written that way, and the general PATTERN they can reuse.

## Teach, don't review

This is the key distinction.

- ✅ Teaching: "Base case stops the recursion — without it, calls never end." Explains the concept so they get it next time.
- ❌ Reviewing: "Bug: missing guard for negative n." Grading their work.

Light correctness/efficiency notes are fine *when they teach something* (e.g. "this is O(2^n) — here's why"), but lead with understanding. No praise/grade filler ("nice work ✔", "good job").

## What to write

For each function or logical block, cover as relevant:

- **What it does** — one plain-language line.
- **The pattern** — name it (recursion, two-pointer, hash map, sliding window, BFS…). Naming lets them recognize it again.
- **Line-level why** — annotate the lines a learner would stumble on: base cases, the "smaller subproblem" step, the tricky index, the combine step.
- **A trace** — walk one small concrete input through the code. This is the highest-value teaching move for recursion/loops.
- **Concept callout** — the transferable idea (e.g. "every recursion needs a base case + a step toward it").
- **Cost when it teaches** — Big-O only if there's a lesson in it (why naive fib is exponential), not as a review checkbox.

## Format

- Edit the file in place with the Edit/Write tools — keep all original code and output.
- Use `#` inline comments (matching the file's language).
- A short header block at top framing the concept is good for a themed file.
- Traces inline right next to the recursive/looping line.
- Keep comments tight — teaching, not an essay. If a comment is longer than the code block it explains, trim it.

## Example (Python, recursion)

```python
# Recursion needs TWO parts: a BASE CASE (when to stop) and a
# RECURSIVE CASE (solve a smaller version, then combine).
def factorial(n):
    if n == 0:            # BASE CASE: 0! = 1. Without this, calls never stop.
        return 1
    return n * factorial(n-1)   # RECURSIVE: shrink n, trust the smaller answer.
    # Trace factorial(3): 3*fact(2) -> 3*2*fact(1) -> 3*2*1*fact(0) -> 6
```

## Don't

- Don't change the code's behavior or "fix" it (mention issues in a comment only if it teaches a concept).
- Don't add grade/praise language.
- Don't over-comment trivial lines (`print(x)  # prints x`).
