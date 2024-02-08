#!/usr/bin/env python3
""" LIFO Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A Lifo caching implementation
    """
    def __init__(selft):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Assign an item to the cache
            if the cache is full, the last item is removed
        """
        if key and item:
            if key not in self.cache_data and\
                    len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_item = list(self.cache_data)[-1]
                self.cache_data.pop(last_item)
                print(f"DISCARD: {last_item}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
