#!/usr/bin/env python3
"""Redis exercice"""

import redis
from typing import Union
from uuid import uuid4


class Cache():
    """ Cach class"""

    def __init__(self):
        """ Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis database"""
        id = str(uuid4())
        self._redis.set(id, data)
        return id
