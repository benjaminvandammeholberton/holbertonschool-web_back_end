#!/usr/bin/env python3

"""
This code snippet defines a function called `to_kv` that takes a string
`k` and a number `v` as input and returns a tuple containing `k` and the
square of `v`.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[str, float]]:
    """
    Calculate the square of a number and return a tuple with the original
    string and the squared value.

    Args:
        k (str): A string representing a key.
        v (Union[int, float]): A number (either an integer or a float).

    Returns:
        tuple[Union[str, float]]: A tuple containing the original string
        `k` and the square of `v`.
    """
    return (k, pow(v, 2))
