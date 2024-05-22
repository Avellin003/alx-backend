#!/usr/bin/env python3
""" Basic Caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Creates a file for storing cache data in value pairs"""

    def __init__(self):
        """ Constructor method"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
