#!/usr/bin/env python3
"""
a python module to implement a simple pagination page
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range - function to find the start & end index of a pagination
    Arguments:
        page: the given page
        page_size: the given page size
    Return:
        tuple with start & end index
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return (start_index, end_index)


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
        """
        get_page - function get a page
        Arguments:
            page: the given page
            page_size: the given page size
        Returns:
            a list of a dataset with that range
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        dst = self.dataset()
        return (dst[start_idx: end_idx])
