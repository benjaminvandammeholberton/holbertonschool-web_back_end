#!/usr/bin/env python3
"""
This code snippet defines a function called `sum_list` that takes in a list
of floats as input and returns the sum of the elements in the list.

Example Usage:
    input_list = [1.5, 2.3, 3.7]
    result = sum_list(input_list)
    print(result)  # Output: 7.5

Inputs:
    input_list (list[float]): A list of floats.

Outputs:
    float: The sum of the elements in the input list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of the elements in the input list.

    Args:
        input_list (list[float]): A list of floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)
