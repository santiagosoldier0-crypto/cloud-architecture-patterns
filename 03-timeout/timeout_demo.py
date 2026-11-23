import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from typing import Callable, TypeVar

T = TypeVar("T")


def call_with_timeout(operation: Callable[[], T], timeout_seconds: float) -> T:
    """Bound caller wait; Python cannot forcibly stop an already-running thread."""
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")
    executor = ThreadPoolExecutor(max_workers=1)
    future = executor.submit(operation)
    try:
        return future.result(timeout=timeout_seconds)
    except TimeoutError as exc:
        future.cancel()
        raise TimeoutError(f"operation exceeded {timeout_seconds}s") from exc
    finally:
        executor.shutdown(wait=False, cancel_futures=True)


if __name__ == "__main__":
    try:
        call_with_timeout(lambda: time.sleep(2), 0.2)
    except TimeoutError as error:
        print(error)
