import threading

from rate_limiter.base import RateLimiter


class ThreadSafeRateLimiter(RateLimiter):
    def __init__(self, wrapped_limiter):
        self._wrapped = wrapped_limiter
        self._lock = threading.Lock()


    def allow(self, key):
        with self._lock:
            return self._wrapped.allow(key)
