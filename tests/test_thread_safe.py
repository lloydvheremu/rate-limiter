import unittest
import threading
from rate_limiter.sliding_window import SlidingWindowRateLimiter
from rate_limiter.thread_safe import ThreadSafeRateLimiter


class TestThreadSafeRateLimiter(unittest.TestCase):
    def test_concurrent_access_respects_limit_exatcly(self):
        inner_limiter = SlidingWindowRateLimiter(max_requests=5, window_seconds=10)
        limiter = ThreadSafeRateLimiter(inner_limiter)

        results = []
        results_lock = threading.Lock()

        def make_request():
            allowed = limiter.allow("user1")
            with results_lock:
                results.append(allowed)

        threads = [threading.Thread(target=make_request) for i in range(50)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
                
        self.assertEqual(results.count(True), 5)
        self.assertEqual(results.count(False), 45)


if __name__ ==  "__main__":
    unittest.main()

