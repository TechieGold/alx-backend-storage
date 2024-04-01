#!/usr/bin/env python3
"""
This module creates a Cache class with and __init__ method that
stores an instance of Redis client as a private varibale and
a store method that takes a data argument and returns a string
"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps


class Cache:
    """ Cache class with two methods (__init__ and store)"""

    def __init__(self):
        """Stores and flush an instance of redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """Returns a Callable"""
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """Creates and returns function that increment the cound for a key
            On every call."""
            self._redis.incr(key)
            return (method(self, *args, **kwargs))
        return (wrapper)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, int, None]:
        """ Retrieves and converts a value to the required format,
            before returning it."""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return (value)

    def get_str(self, key: str) -> Union[str, None]:
        """Retrives value, decode it as UTF-8 and return a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """ Retrives value, converts to an integer before returining it."""
        return self.get(key, fn=int)
