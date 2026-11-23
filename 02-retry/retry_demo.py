import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry(operation: Callable[[], T], max_retries: int = 3, base_delay: float = 0.1,
          sleep: Callable[[float], None] = time.sleep) -> T:
    """Initial call plus up to max_retries; delays double after each failure."""
    if max_retries < 0 or base_delay < 0:
        raise ValueError("retry count and base delay must be non-negative")
    for attempt in range(max_retries + 1):
        try:
            return operation()
        except Exception:
            if attempt == max_retries:
                raise
            sleep(base_delay * (2 ** attempt))
    raise AssertionError("unreachable")


if __name__ == "__main__":
    attempts = 0

    def flaky_service():
        global attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError("temporary failure")
        return "ok"

    print(retry(flaky_service))
    print(f"intentos: {attempts}")
