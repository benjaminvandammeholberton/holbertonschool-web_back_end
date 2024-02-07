#!/usr/bin/env python3
""" FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A FIFO caching implementation
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
            if the cache is full, the first item is removed
        """
        if key not in self.cache_data and len(self.cache_data)\
                == BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD {first_key}")
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
