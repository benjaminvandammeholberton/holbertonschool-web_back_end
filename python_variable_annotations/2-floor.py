#!/usr/bin/env python3
"""
This code snippet defines a function called 'floor' that takes a float
number as input and returns the largest integer less than or equal to
the input number.
"""

import math


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the input float number.

    Args:
        n (float): The input float number.

    Returns:
        int: The largest integer less than or equal to the input float number.
    """
    return math.floor(n)
