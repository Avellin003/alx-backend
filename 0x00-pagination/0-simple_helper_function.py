#!/usr/bin/env python3
"index_range definition"
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    begin, end = 0, 0
    for i in range(page):
        begin = end
        end += page_size

    return (begin, end)
