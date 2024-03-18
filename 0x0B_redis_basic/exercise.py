#!/usr/bin/env python3
"""Redis exercice"""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache():
    """ Cach class"""

    def __init__(self) -> None:
        """ Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis database"""
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    int,
                                                                    bytes,
                                                                    float,
                                                                    None]:
        """get method for redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            (value) = fn(value)

    def get_int(self, value: str) -> int:
        """parametrize get method with the int conversion function"""
        return self.get(value, int)

    def get_string(self, value: str) -> str:
        """parametrize get method with the string conversion function"""
        return lambda value: value.decode("utf-8")
