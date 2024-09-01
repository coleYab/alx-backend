#!/usr/bin/env python3
"""
A Module to hold the helper function
"""

import typing

def index_range(page: int, page_size: int) -> typing.Tuple[int]:
    """function to count the range of the items to be returned

    Args:
        page (int): the page count
        page_size (int): the page size

    Raises:
        Exception: index is invalid 

    Returns:
        typing.Tuple[int]: _description_
    """
    if page <= 0:
        raise Exception("Invalid index")
    return ((page - 1) * page_size, page * page_size)