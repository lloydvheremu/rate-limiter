import unittest
from rate_limiter.sliding_window import SlidingWindowRateLimiter


class TestSlidingWindowRateLimiter(unittest.TestCase):
    def test_first_request_is_allowed(self):
        limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10)
        self.assertTrue(limiter.allow("user1"))

if __name__ == "__main__":
    unittest.main()
