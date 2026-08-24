import unittest
from rate_limiter.sliding_window import SlidingWindowRateLimiter


class TestSlidingWindowRateLimiter(unittest.TestCase):
    def test_first_request_is_allowed(self):
        limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10)
        self.assertTrue(limiter.allow("user1"))

    def test_requests_beyond_limit_are_rejected(self):
        limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10)
        self.assertTrue(limiter.allow("user1"))
        self.assertTrue(limiter.allow("user1"))
        self.assertTrue(limiter.allow("user1"))
        self.assertFalse(limiter.allow("user1"))
    def test_request_allowed_after_window_slides(self):
        current_time = [1000.0]
        clock = lambda: current_time[0]

        limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10, clock=clock)

        limiter.allow("user1")
        limiter.allow("user1")
        limiter.allow("user1")
        self.assertFalse(limiter.allow("user1")) #4th call, still within window, reject.

        current_time[0] = 1011.0 # simulate 11 seconds passing
        self.assertTrue(limiter.allow("user1")) # old requests aged out, allowed again.
    def test_different_keys_are_limited_independently(self):
        limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=10)

        self.assertTrue(limiter.allow("user1"))
        self.assertTrue(limiter.allow("user1"))
        self.assertFalse(limiter.allow("user1")) # =user now at limit

        self.assertTrue(limiter.allow("user2"))
        self.assertTrue(limiter.allow("user2"))
        self.assertFalse(limiter.allow("user2"))

if __name__ == "__main__":
     unittest.main() 

