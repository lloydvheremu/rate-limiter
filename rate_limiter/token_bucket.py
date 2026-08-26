from enum import show_flag_values
from rate_limiter.base import RateLimiter
import time

class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, max_requests, window_seconds, clock=None):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._clock = clock or time.time 
        self._buckets = {}
        self._refill_rate = max_requests / window_seconds

    def allow(self, key):
        now = self._clock()
        tokens, last_check = self._buckets.get(key, (self.max_requests, now))

        elapsed = now - last_check
        refilled = elapsed * self._refill_rate
        tokens = min(self.max_requests, tokens + refilled)

        if tokens >= 1:
            tokens -= 1
            self._buckets[key] = (tokens, now)
            return True

        self._buckets[key] = (tokens, now)        
        return False
