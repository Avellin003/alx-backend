#!/usr/bin/env python3
"""Importation of BaseCaching module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out Caching system"""

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
                discard_key = BaseCaching.MAX_ITEMS - 1
                print("DISCARD: {}".format(self.order[discard_key]))
                # Prints the deleted cache
                # Deletes the last in key which has location 0 in order
                del self.cache_data[self.order[discard_key]]
                # Deletes the item related to the last in key
                del self.order[discard_key]
            self.order.append(key)
            # Appends the new key in the order list
            self.cache_data[key] = item
            # Assigns a value to it

    def get(self, key):
        """Returns the key value from the cache storage"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
