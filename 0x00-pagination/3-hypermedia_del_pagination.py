#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
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
        """Getting indexed hyper mmidea data
        """
        index_ds = self.indexed_dataset()
        assert index >= 0 and index < len(index_ds)
        start, end = index_range(index, page_size)

        data = []

        if start < len(index_ds.values()):
            if end <= len(index_ds.values()):
                data = list(index_ds.items())[start:end]
            else:
                data = list(index_ds.items())[start:]

        indexed_data = {
            'index': index if len(data) == 0 else data[0][0],
            'data': [i[1] for i in data],
            'page_size': len(data),
            'next_index': index + page_size if len(data) else data[-1][0] + 1
        }

        return indexed_data


def index_range(index: int, page_size: int) -> Tuple[int]:
    """function to count the range of the items to be returned

    Args:
        page (int): the index to retrive
        page_size (int): the page size

    Raises:
        Exception: index is invalid

    Returns:
        Tuple[int]: _description_
    """
    return (index, index + page_size)
