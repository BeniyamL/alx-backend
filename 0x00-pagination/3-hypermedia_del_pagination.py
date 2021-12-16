#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        get_hyper_index - function to get the extract record from index
        Arguments:
            index: the current start index of the return page
            page_size: the given page size
        Return:
            Dictionary with key-value pair of index, next_index,
            page_size & data
        """
        try:
            dst: List = self.indexed_dataset()
        except AssertionError:
            return {}
        dst_keys = list(dst.keys())
        last_idx = len(dst_keys) - 1
        assert index > 0 and index < last_idx
        data: List = []

        if index in dst_keys:
            start_idx = index
        else:
            start_idx = dst_keys[index]

        for i in range(start_idx, start_idx + page_size):
            data.append(dst[i])

        page_size = len(data)
        nxt_idx: int = start_idx + page_size

        page: Dict = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": nxt_idx
        }
        return page
