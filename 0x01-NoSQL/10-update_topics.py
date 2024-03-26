#!/usr/bin/env python3
""" Contains function that changes all topics of a school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document based on the name.
    
    Args:
        mongo_collection: the pymongo collection object,
        name: School name to update.
        topics: List of topics approached in the school.
    """
    mongo_collection.update_many({"name": name},{"$set": {"topics": topics}})
