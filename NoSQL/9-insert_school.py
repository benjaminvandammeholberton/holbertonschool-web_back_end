#!/usr/bin/env python3
"""
This code snippet defines a function called 'insert_school' that inserts a document into a MongoDB collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a document into a MongoDB collection.

    Parameters:
    - mongo_collection (MongoDB collection): The collection where the document will be inserted.
    - **kwargs (keyword arguments): The document data to be inserted. It can be any number of key-value pairs.

    Returns:
    - inserted_id (ObjectId): The ID of the inserted document in the MongoDB collection.
    """
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
