#!/usr/bin/python3
"""
FIFO Module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """a FIFO cache class"""
    def __init__(self):
        """
        init method to overload the parent init method
        """
        super().__init__()

    def put(self, key, item):
        """
        put - method to insert a new item at index key
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
                    cach_lst = list(self.cache_data.keys())
                    frst_key = cach_lst[0]
                    del self.cache_data[frst_key]
                    print("DISCARD: {}".format(frst_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        get - function to get the value at key index
        Arguments:
            key: the given key
        Returns:
            the item at key index
        """
        return self.cache_data.get(key)
