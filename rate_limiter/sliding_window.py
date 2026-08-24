class SlidingWindowRateLimiter:
    def __init__(self, max_requests, window_seconds, clock=None):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests = {}

    def allow(self, key):
        return True
