#!/usr/bin/env python3
"""
simple pagination element
"""

import csv
import math
from typing import List, Tuple


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
        """returns a page of baby names
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index_rng = index_range(page, page_size)
        data_set = self.dataset()
        page_data = []

        if index_rng[0] <= len(data_set) - 1:
            if index_rng[1] > len(data_set) - 1:
                return data_set[index_rng[0]:]
            page_data = data_set[index_rng[0]:index_rng[1]]

        return page_data


    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """generateing some hyper midea infromations for a page
        """
        total_pages = math.floor(len(self.dataset()) / page_size)
        if len(self.dataset()) % page_size != 0:
            total_pages += 1
        data = self.get_page(page, page_size)
        hyper_midea = {
            'page_size': len(data), 'page': page, 'data': data,
            'next_page': page + 1, 'prev_page': page - 1, 'total_pages': total_pages
          }

        return hyper_midea


def index_range(page: int, page_size: int) -> Tuple[int]:
    """function to count the range of the items to be returned

    Args:
        page (int): the page count
        page_size (int): the page size

    Raises:
        Exception: index is invalid

    Returns:
        Tuple[int]: _description_
    """
    assert page_size > 0 and page > 0
    return ((page - 1) * page_size, page * page_size)
