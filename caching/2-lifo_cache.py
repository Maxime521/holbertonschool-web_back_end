#!/usr/bin/python3
""" LIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system
    """
    def __init__(self):
        """ Initialize the LIFO Cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
