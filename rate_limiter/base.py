
from abc import ABC, abstractmethod


class RateLimiter(ABC):
    @abstractmethod
    def allow(self, key):
        """ Return True if the request for this key is allowed"""
        raise NotImplementedError


