#!/usr/bin/env python3
# initial code for python3 in my world

import typing

def index_range(page: int, page_size: int) -> typing.Tuple[int]:
    if page <= 0:
        raise Exception("Invalid index")
    return ((page - 1) * page_size, page * page_size)