#!/usr/bin/env python3
"""
a python module to implement a hyper media pagination page
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_page - function get a page
        Arguments:
            page: the given page
            page_size: the given page size
        Returns:
            a dictionary containing key-value pair of
            page_size, page, data, next_page, prev_page, total_pages
        """
        dst: List = self.dataset()
        if dst:
            total_rcrd: int = len(dst)
        else:
            total_rcrd: int = 0
        try:
            data: List = self.get_page(page, page_size)
        except AssertionError:
            return {}
        total_pg: int = math.ceil(total_rcrd / page_size)
        if (page + 1 > total_pg):
            next_pg: int = None
        else:
            next_pg: int = page + 1

        if (page - 1 <= 0):
            prev_pg: int = None
        else:
            prev_pg: int = page - 1

        if len(data) == 0:
            page_size = 0
        page: Dict = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_pg,
            "prev_page": prev_pg,
            "total_pages": total_pg
        }
        return page
