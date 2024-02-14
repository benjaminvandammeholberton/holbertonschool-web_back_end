#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Finds the correct indexes to paginate dataset correctly"""
    assert type(page) is int
    assert page > 0
    assert type(page_size) is int
    assert page_size > 0
    indexes = index_range(page, page_size)
    return self.dataset()[indexes[0]:indexes[1]]
