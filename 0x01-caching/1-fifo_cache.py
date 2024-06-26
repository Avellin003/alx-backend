#!/usr/bin/env python3
"""Importation of BaseCaching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ First In First Out Caching system"""

    def __init__(self):
        """Constructor method"""
        super().__init__()
        # Call the parent's class constructor
        self.order = []
        # Create a list to store order of keys

    def put(self, key, item):
        """Putting new value pairs in cache"""
        if key is None or item is None:
            # Checks if key or item are not in cache
            pass
        else:
            length = len(self.cache_data)
            # Gets the total length of Cache
            # Checks if the new key is in cache and If cache storage is full
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                # Prints the deleted cache
                # Deletes the first in key which has location 0 in order
                del self.cache_data[self.order[0]]
                # Deletes the item related to the first in key
                del self.order[0]
            self.order.append(key)
            # Appends the new key in the order list
            self.cache_data[key] = item
            # Assigns a value to it

    def get(self, key):
        """Returns the key value from the cache storage"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
