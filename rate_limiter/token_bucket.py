from enum import show_flag_values
from rate_limiter.base import RateLimiter
import time

class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, max_requests, window_seconds, clock=None):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._clock = clock or time.time 
        self._buckets = {}

    def allow(self, key):
        return True


