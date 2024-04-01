#!/usr/bin/env python3
"""web cache and tracker"""

import requests
import redis
from functools import wraps
from typing import Callable

redis = redis.Redis()


def count_url_access(fn: callable) -> callable:
    """Decorator counting how many times a URL is accessed"""
    @wraps(fn)
    def wrapper(url):
        redis.incr(f"count:{url}")
        cached_resp = redis.get(f"cached:{url}")
        if cached_resp:
            return (cached_resp.decode('utf-8'))
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return (result)
    return (wrapper)


@count_url_access
def get_page(url: str) -> str:
    """Returns HTML content of a url"""
    resp = requests.get(url)
    return (resp.text)
