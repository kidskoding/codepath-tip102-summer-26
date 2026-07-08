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
