from enum import Enum
from typing import Callable, TypeVar

T = TypeVar("T")


class State(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF-OPEN"


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 2) -> None:
        if failure_threshold < 1:
            raise ValueError("failure_threshold must be positive")
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.state = State.CLOSED

    def call(self, operation: Callable[[], T]) -> T:
        if self.state is State.OPEN:
            self.state = State.HALF_OPEN
        try:
            result = operation()
        except Exception:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.state = State.OPEN
            raise
        self.failures = 0
        self.state = State.CLOSED
        return result


if __name__ == "__main__":
    breaker = CircuitBreaker()
    for attempt in range(3):
        try:
            breaker.call(lambda: (_ for _ in ()).throw(ConnectionError("service unavailable")))
        except ConnectionError:
            print(f"fallo {attempt + 1}: {breaker.state.value}")
    def healthy_probe():
        print("probe state:", breaker.state.value)
        return "ok"

    print("probe:", breaker.call(healthy_probe), breaker.state.value)
