#!/usr/bin/env python3
"""
This code snippet defines a function called 'list_all' that takes a MongoDB
collection as input and returns all the documents in that collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
