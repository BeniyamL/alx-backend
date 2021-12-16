#!/usr/bin/env python3
"""
a python module to rutn a tubple of size two contaning
a start & end index corresponding to the range
"""


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
