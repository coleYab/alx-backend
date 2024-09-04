#!/usr/bin/env python3
"""
Base cache implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    a class to represent basic caching features
    """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.lru_items_list = []

    def put(self, key, item):
        """ adding a cache to chached data
        """
        if None not in [key, item]:
            if key in self.lru_items_list:
                self.lru_items_list.remove(key)
            if len(self.lru_items_list) == BaseCaching.MAX_ITEMS:
                discarded = self.lru_items_list.pop(self.MAX_ITEMS - 1)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

            self.lru_items_list.insert(0, key)
            self.cache_data[key] = item


    def get(self, key):
        """ retriving a cache with the key
        """
        if key in self.cache_data:
            self.lru_items_list.remove(key)
            self.lru_items_list.insert(0, key)
            return self.cache_data[key]
