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

def call_history(method: Callable) -> Callable:
    """ create input and output list keys, respectively."""
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return (res)
    return (wrapper)

def replay(fn: Callable):
    '''display the history of calls of a particular function.'''
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))



class Cache:
    """ Cache class with two methods (__init__ and store)"""

    def __init__(self):
        """Stores and flush an instance of redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
