#!/usr/bin/python3
""" MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system
    """
    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key = self.order.pop()
            del self.cache_data[most_recent_key]
            print("DISCARD: {}".format(most_recent_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
