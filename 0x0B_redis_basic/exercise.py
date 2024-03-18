#!/usr/bin/env python3
"""Redis exercice"""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function
    """
    method_name = method.__qualname__
    r = redis.Redis()

    input = f'{method_name}:inputs'
    output = f'{method_name}:outputs'

    inputs = r.lrange(input, 0, -1)
    outputs = r.lrange(output, 0, -1)

    in_ou = list(zip(inputs, outputs))
    print(f'{method_name} was called {len(in_ou)} times:')
    for element in in_ou:
        print(
            f'{method_name}(*{element[0].decode("utf-8")}) ->\
                {element[1].decode("utf-8")}'
        )


def count_calls(method: Callable) -> Callable:
    """
    Count how many times methods of the Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        Increments the count of the method
        """
        self._redis.incr(key)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs for a particular function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        Store the inputs and outputs in redis
        """
        self._redis.rpush(f'{key}:inputs', str(args))
        id = method(self, str(args))
        self._redis.rpush(f'{key}:outputs', str(id))
        return id

    return wrapper


class Cache():
    """ Cach class based on redis"""

    def __init__(self) -> None:
        """ Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis database"""
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float,
                                                                    None]:
        """get method for redis"""
        value = self._redis.get(key)
        if not value:
            return None

        if fn:
            value = fn(value)

        return value

    def get_int(self, key: str) -> int:
        """Parametrizes get with the correct conversion function"""
        return self.get(key, int)

    def get_str(self, key: str) -> str:
        """Parametrizes get with the correct conversion function"""
        return self.get(key, lambda value: value.decode("utf-8"))
