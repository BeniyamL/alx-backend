#!/usr/bin/python3
"""
Least recently used module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    a class to implement LRU cache policy
    """
    def __init__(self):
        """
        init method to overload the paranet init method
        """
        super().__init__()
        self.recent_cache = []

    def put(self, key, item):
        """
        put - function to insert the new item using LRU algorithm
        Arguments:
            key: the given key
            item: the given item
        Returns:
            nothing
        """
        if (key and item):
            val = self.cache_data.get(key)
            if val is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    rcnt_key = self.recent_cache[0]
                    del self.cache_data[rcnt_key]
                    self.recent_cache.remove(rcnt_key)
                    print("DISCARD: {}".format(rcnt_key))

            else:
                del self.cache_data[key]
            self.cache_data[key] = item
            if key in self.recent_cache:
                self.recent_cache.remove(key)
                self.recent_cache.append(key)
            else:
                self.recent_cache.append(key)

    def get(self, key):
        """
        get - function to get the item at a given index key
        Arguments:
            key: the given key
        Returns:
            the item at a key index
        """
        val = self.cache_data.get(key)
        if val:
            self.recent_cache.remove(key)
            self.recent_cache.append(key)
        return val
