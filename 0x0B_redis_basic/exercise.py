#!/usr/bin/env python3
"""Redis exercice"""

from uuid import uuid4
import redis


class Cache():
    """ Cach class"""

    def __init__(self):
        """ Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Store data in redis database"""
        if (
                data is isinstance(str) or
                data is isinstance(bytes) or
                data is isinstance(int) or
                data is isinstance(float)
        ):
            id = str(uuid4())
            self._redis.set(id, data)
            return id
