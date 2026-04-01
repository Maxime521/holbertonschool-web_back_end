#!/usr/bin/env python3
"""
Cache class using Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called using Redis.

    Uses the method's __qualname__ as the key in Redis to track call counts.

    Args:
        method: The method to be decorated

    Returns:
        The wrapped method that increments the call count
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count in Redis."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs in Redis.

    Stores inputs in {qualname}:inputs and outputs in {qualname}:outputs lists.

    Args:
        method: The method to be decorated

    Returns:
        The wrapped method that stores input/output history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores input and output history in Redis."""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        # Store input arguments as string
        self._redis.rpush(input_key, str(args))

        # Execute the original method and get output
        output = method(self, *args, **kwargs)

        # Store output as string
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


class Cache:
    """Cache class that stores data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key

        Args:
            data: Data to store (str, bytes, int, or float)

        Returns:
            str: The generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the provided key and optionally convert.

        Args:
            key: The key to retrieve data for
            fn: Optional callable to convert the data to desired format

        Returns:
            The data retrieved from Redis, optionally converted by fn.
            Returns None if key doesn't exist (preserves Redis.get behavior)
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and convert it to a UTF-8 string.

        Args:
            key: The key to retrieve data for

        Returns:
            The data as a UTF-8 string, or None if key doesn't exist
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.

        Args:
            key: The key to retrieve data for

        Returns:
            The data as an integer, or None if key doesn't exist
        """
        return self.get(key, fn=int)
