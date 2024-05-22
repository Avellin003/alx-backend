#!/usr/bin/env python3
"""Importing the BaseCaching Module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Last Frequently Used Caching system"""

    def __init__(self):
        """Initialize BaseCaching attributes"""
        super().__init__()
        # Create a list to store the order usage of keys
        self.usage = []
        # Create a dictionary to store the frequency of keys
        self.frequency = {}

    def put(self, key, item):
        """Adds new Cache items"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Checks if the new key is not already in cache
                # Checks if cache storage is full
                lf_used = min(self.frequency.values())
                #Checks the least used key
                lf_keys = []
                # Create a list to store the least used keys
                # If there are more than one key with the same frequency
                for a, b in self.frequency.items():
                    if b == lf_used:
                        lf_keys.append(a)
                if len(lf_keys) > 1:
                    lr_lf_used = {}
                    for a in lf_keys:
                        lr_lf_used[a] = self.usage.index(a)
                    discard = min(lr_lf_used.values())
                    discard = self.usage[discard]
                else:
                    discard = lf_keys[0]
                # Deletes the least used key
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            # Adds a new key and item
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Allows the deletion of selected key by user"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
