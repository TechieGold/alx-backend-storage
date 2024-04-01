#!/usr/bin/env python3
"""
This module creates a Cache class with and __init__ method that
stores an instance of Redis client as a private varibale and
a store method that takes a data argument and returns a string
"""
import redis
from typing import Union
import uuid


class Cache:
    """ Cache class with two methods (__init__ and store)"""
    def __init__(self):
        """Stores and flush an instance of redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
