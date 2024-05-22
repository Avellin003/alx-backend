#!/usr/bin/env python3
"""Importing the BaseCaching Module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used Caching system"""
    def __init__(self):
        """Initialize BaseCaching attributes"""
        super().__init__()
        # Create a list to store the order usage of keys
        self.usage = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Checks if the new key is not already in cache
                # Checks if cache storage is full
                most = BaseCaching.MAX_ITEMS - 1
                print("DISCARD: {}".format(self.usage[most]))
                # Prints the deleted cache
                del self.cache_data[self.usage[most]]
                # Deletes the most used key
                del self.usage[most]
                # Deletes the Item related to the most used key
            if key in self.usage:
                del self.usage[self.usage.index(key)]
                # Adds a new key and item
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Allows the deletion of selected key by user"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
