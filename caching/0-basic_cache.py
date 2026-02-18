#!/usr/bin/python3
""" BasicCache module
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
        Inherits from BaseCaching
        Implements a cache with no limit on storage
    """

    def put(self, key, item):
        """ Add an item to the cache
            Args:
            key: the key to identify the item
            item: the value to store
            Note: Does nothing if key or item is None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache
            Args:
            key: the key to look up
            Returns:
            The value associated with key, or None if not found
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
