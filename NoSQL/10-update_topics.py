#!/usr/bin/env python3
"""A function that updates the 'topics' field in a MongoDB collection based on
the 'name' field.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field in a MongoDB collection based on the 'name'
    field.
    """
    if mongo_collection is None:
        return None
    return mongo_collection.update_many({"name": name}, {"$set": {"topics":
                                                                  topics}})
