#!/usr/bin/env python3
"""
This is a function called `element_length` that takes a list of strings
as input and calculates the length of each element in the list. It returns
a new list of tuples, where each tuple contains an element from the input
list and its corresponding length.

Example Usage:
lst = ['apple', 'banana', 'cherry']
result = element_length(lst)
print(result)
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input list.

    Args:
        lst (List[str]): A list of strings for which to calculate element
        lengths.

    Returns:
        List[Tuple[str, int]]: A list of tuples, where each tuple contains an
        element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
