#!/usr/bin/env python3
"""
This code snippet defines a function called `make_multiplier` that
takes a `multiplier` value as input and returns a function. 
The returned function takes a `second_multiplier` value as input and
returns the product of the two multipliers.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by the provided multiplier.

    Parameters:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that takes a number as input and
    returns the product of the multiplier and the input number.
    """
    def f(second_multiplier: float) -> float:
        """
        Returns the product of the multiplier and the second_multiplier.

        Parameters:
        second_multiplier (float): The second multiplier value.

        Returns:
        float: The product of the multiplier and the second_multiplier.
        """
        return multiplier * second_multiplier
    return f
