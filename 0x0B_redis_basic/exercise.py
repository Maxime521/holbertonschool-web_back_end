#!/usr/bin/env python3
"""
Cache class using Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class that stores data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
