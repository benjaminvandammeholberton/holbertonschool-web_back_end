#!/usr/bin/env python3
""" MRU Caching
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ A MRU caching implementation
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
            If the cache is full, the most recently used item is removed
        """
        if key and item:
            if key not in self.cache_data and\
                    len(self.cache_data) == BaseCaching.MAX_ITEMS:
                item_to_remove = self.cache_data.popitem()
                print(f"DISCARD: {item_to_remove[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
