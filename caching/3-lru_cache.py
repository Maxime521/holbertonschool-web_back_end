#!/usr/bin/python3
""" LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system
    """
    def __init__(self):
        """ Initialize the LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_recent_key = self.order.pop(0)
            del self.cache_data[least_recent_key]
            print("DISCARD: {}".format(least_recent_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
