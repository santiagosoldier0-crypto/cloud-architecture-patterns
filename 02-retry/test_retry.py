import pytest

from retry_demo import retry


def test_retries_with_exponential_delays_then_succeeds():
    attempts, delays = 0, []

    def operation():
        nonlocal attempts
        attempts += 1
        if attempts < 4:
            raise ConnectionError("temporary")
        return "ok"

    assert retry(operation, sleep=delays.append, base_delay=0.25) == "ok"
    assert attempts == 4
    assert delays == [0.25, 0.5, 1.0]


def test_stops_after_three_retries():
    attempts = 0

    def fail():
        nonlocal attempts
        attempts += 1
        raise TimeoutError()

    with pytest.raises(TimeoutError):
        retry(fail, sleep=lambda _: None)
    assert attempts == 4
