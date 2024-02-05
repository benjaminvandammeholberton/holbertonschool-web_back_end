#!/usr/bin/env python3
"""
Module that defines "safely_get_value"
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')
def safely_get_value(dct: Mapping , key: Any, default: Union[T, None] = None)->Union[Any, T]:
    """
    Function that returns a value of a key in a dict
    """
    if key in dct:
        return dct[key]
    else:
        return default