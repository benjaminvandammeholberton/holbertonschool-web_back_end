#!/usr/bin/env python3
""" LFU Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ A LFU caching implementation
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    print("DISCARD: ")
                    
                else:
                    self.cache_data[key] = [item, 0]

            else:
                self.cache_data[key][0] = item

    def get(self, key):
        """
        """
        if key and key in self.cache_data:
            
            return self.cache_data.get(key)[0]
        return None
