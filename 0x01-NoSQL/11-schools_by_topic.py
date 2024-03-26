#!/usr/bin/env python3
""" Contains function that returns list of school having specific topic."""


def school_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    
    Args:
        mongo_collection: pymongo collection object.
        topic: topic to be searched.
    """
    return mongo_collection.find({"topics": topic})
