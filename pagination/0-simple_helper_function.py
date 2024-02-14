#!/usr/bin/env python3
"""
Calculates the starting and ending indices for a given page in a paginated
data set.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the starting and ending indices for a given page in a paginated
    data set.

    Args:
        page (int): The page number for which to calculate the indices.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the starting and ending indices.
    """
    index_start = page * page_size - page_size
    index_end = page * page_size

    return (index_start, index_end)
