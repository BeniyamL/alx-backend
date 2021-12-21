#!/usr/bin/python3
"""
a LIFO Module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    a class for lifo cache impelementation
    """
    def __init__(self):
        """
        init method to overload the parent init method
        """
        super().__init__()

    def put(self, key, item):
        """
        put - function to insert the new item into the cache
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
                    cache_lst = list(self.cache_data.keys())
                    lst_key = cache_lst[len(self.cache_data) - 1]
                    del self.cache_data[lst_key]
                    print("DISCARD: {}".format(lst_key))
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        get - function to get value at a index key
        Arguments:
            key: the given key
        Returns:
            the item value at a given key index
        """
        return self.cache_data.get(key)
