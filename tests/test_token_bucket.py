import unittest
from rate_limiter.token_bucket import TokenBucketRateLimiter


class TestTokenBucketRateLimiter(unittest.TestCase):
    def test_first_request_is_allowed(self):
        limiter = TokenBucketRateLimiter(max_requests=3, window_seconds=10)
        self.assertTrue(limiter.allow("user1"))

    def test_requests_beyond_capacity_are_rejected(self):
        limiter = TokenBucketRateLimiter(max_requests=3, window_seconds=10)
        self.assertTrue(limiter.allow("user1"))
        self.assertTrue(limiter.allow("user1"))
        self.assertTrue(limiter.allow("user1"))
        self.assertFalse(limiter.allow("user1"))

if __name__ == "__main__":
    unittest.main()


