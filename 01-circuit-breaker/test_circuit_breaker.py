import pytest

from circuit_breaker import CircuitBreaker, State


def test_transitions_closed_open_half_open_and_closed():
    breaker = CircuitBreaker(failure_threshold=2)
    failing = lambda: (_ for _ in ()).throw(ConnectionError("down"))
    with pytest.raises(ConnectionError):
        breaker.call(failing)
    assert breaker.state is State.CLOSED
    with pytest.raises(ConnectionError):
        breaker.call(failing)
    assert breaker.state is State.OPEN
    observed = []
    assert breaker.call(lambda: (observed.append(breaker.state), "recovered")[1]) == "recovered"
    assert observed == [State.HALF_OPEN]
    assert breaker.state is State.CLOSED


def test_rejects_invalid_threshold():
    with pytest.raises(ValueError):
        CircuitBreaker(0)
