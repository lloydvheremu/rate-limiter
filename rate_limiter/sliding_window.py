import time

class SlidingWindowRateLimiter:
    def __init__(self, max_requests, window_seconds, clock=None):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests = {}
        self._clock = clock or time.time

    def allow(self, key):
        now = self._clock()
        window_start = now - self.window_seconds
        timestamps = self._requests.get(key, [])
        timestamps = [t for t in timestamps if t > window_start]

        if len(timestamps) < self.max_requests:
            timestamps.append(now)
            self._requests[key] = timestamps
            return True

        self._requests[key] = timestamps
        return False

    def cleanup(self):
        now = self._clock()
        window_start = now - self.window_seconds

        expired_keys = [
            key for key, timestamps in self._requests.items()
            if not [t for t in timestamps if t > window_start]

        ]

        for key in expired_keys:
            del self._requests[key] # Note to self, in production this data may be saved to primary storage for analytics.
            

