#!/usr/bin/env python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A basic caching implementation
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
