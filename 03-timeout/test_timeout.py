import time
from concurrent.futures import TimeoutError

import pytest

from timeout_demo import call_with_timeout


def test_slow_operation_times_out():
    with pytest.raises(TimeoutError, match="exceeded"):
        call_with_timeout(lambda: time.sleep(0.2), 0.01)


def test_fast_operation_returns_result():
    assert call_with_timeout(lambda: "ok", 1) == "ok"
