#!/usr/bin/env python3
"""
This code snippet defines a function called `schools_by_topic` that searches
for documents in a MongoDB collection based on a specified topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Searches for documents in a MongoDB collection based on a specified topic.

    Parameters:
    - mongo_collection (MongoDB collection): The collection to search for
    documents in.
    - topic (str): The topic to search for in the "topics" field of the
    documents.

    Returns:
    - A cursor object that represents the result of the search. This cursor
    can be iterated over to access the matching documents.
    """
    if mongo_collection is None:
        return None
    return mongo_collection.find({"topics": topic})
