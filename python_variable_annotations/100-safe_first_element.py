#!/usr/bin/env python3
"""
This module defines safe_first_element function
"""
from typing import Sequence, Any, Union
def safe_first_element(lst: Sequence[Any])-> Union[Any, None]:
    """
    Function that returns the first element of a sequence

    Args:
        lst: the sequence we need to extract the first element
    
    Returns: The first element if the argument exists, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
