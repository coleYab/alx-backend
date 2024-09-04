#!/usr/bin/env python3
"""
Base cache implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    a class to represent basic caching features
    """
    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ adding a cache to chached data
        """
        if None not in [key, item]:
            if len(self.cache_data.items()) == BaseCaching.MAX_ITEMS:
                discard = list(self.cache_data.keys())[-1]
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item

    def get(self, key):
        """ retriving a cache with the key
        """
        if key in self.cache_data:
            return self.cache_data[key]
