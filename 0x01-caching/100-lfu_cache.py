#!/usr/bin/python3
"""
least frequently used module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    a class to implement LFU cache policy
    """
    def __init__(self):
        """
        init method to overload the paranet init method
        """
        super().__init__()
        self.recent_cache = {}

    def put(self, key, item):
        """
        put - function to insert the new item using LFU algorithm
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
                    s_dic = dict(
                        sorted(self.recent_cache.items(), key=lambda x: x[1])
                        )
                    rcnt_key = list(s_dic.keys())[0]
                    del self.cache_data[rcnt_key]
                    del self.recent_cache[rcnt_key]
                    print("DISCARD: {}".format(rcnt_key))

            else:
                del self.cache_data[key]
            self.cache_data[key] = item
            if key in self.recent_cache:
                self.recent_cache[key] += 1
            else:
                self.recent_cache[key] = 1

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
            if key in self.recent_cache:
                self.recent_cache[key] += 1
            else:
                self.recent_cache[key] = 1
        return val
