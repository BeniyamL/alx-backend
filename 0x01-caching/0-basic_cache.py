#!/usr/bin/env python3
"""
a python module for creating basic cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a Basic cache class
    """
    def put(self, key, item):
        """
        put - method for putting the item value with key
        Arguments:
            key: the given key
            item: the item to be inserted
        Returns:
            nothing
        """
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """
        get - function to get the item
        Arguments:
            key: the given key
        Returns:
            the item at a index key
        """
        item = self.cache_data.get(key)
        return (item)
