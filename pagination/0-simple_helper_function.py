#!/usr/bin/env python3
""" Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = page - 1 * page_size
    end_index = page_size * page
    return (start_index, end_index)
