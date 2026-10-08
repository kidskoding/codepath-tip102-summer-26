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
