#!/usr/bin/env python3
"""List all documents in a collection. """

def list_all(mongo_collection):
    """ List all collection, return an empty list if none """
    return mongo_collection.find()
