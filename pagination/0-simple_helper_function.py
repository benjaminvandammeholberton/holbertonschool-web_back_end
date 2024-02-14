#!/usr/bin/env python3
""" 
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculates the starting and ending indices for a given page in a paginated
    data set.

    Args:
        page (int): The page number for which to calculate the indices.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the starting and ending indices.
    """
    start_index = page * page_size - page_size
    end_index = page_size * page
    return (start_index, end_index)
