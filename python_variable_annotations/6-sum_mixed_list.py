#!/usr/bin/env python3
"""
This code snippet defines a function called `sum_mixed_list` that takes a list
of mixed integers and floats as input and returns the sum of all the elements
in the list as a float.

Example Usage:
    mixed_list = [1, 2.5, 3, 4.7]
    result = sum_mixed_list(mixed_list)
    print(result)  # Output: 11.2

Inputs:
    mxd_lst (List[Union[int, float]]): A list of mixed integers and floats.

Outputs:
    float: The sum of all the elements in the input list as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all the elements in the input list.

    Args:
        mxd_lst (List[Union[int, float]]): A list of mixed integers and floats.

    Returns:
        float: The sum of all the elements in the input list as a float.
    """
    return sum(mxd_lst)
