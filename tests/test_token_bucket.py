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

    def test_tokens_refill_over_time(self):
        current_time = [1000.0]
        clock = lambda: current_time[0]

        limiter = TokenBucketRateLimiter(max_requests=3, window_seconds=10, clock=clock)

        limiter.allow("user1")
        limiter.allow("user1")
        limiter.allow("user1")
        self.assertFalse(limiter.allow("user1")) # bucket empty 

        current_time[0] = 1004.0 # 4 seconds later, aprrox 1.2 tokens refilled 
        self.assertTrue(limiter.allow("user1")) # enough for one request 
        self.assertFalse(limiter.allow("user1")) # but not for two 

if __name__ == "__main__":
    unittest.main()

