#!/usr/bin/env python3
"""hypermedia del pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """cache dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                data = [row for row in read]
            self.__dataset = data[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """cache indexed dataset"""
        if self.__indexed_dataset is None:
            data = self.dataset()
            truncated_dataset = data[:1000]
            self.__indexed_dataset = {
                i: data[i] for i in range(len(data))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get hyper index"""
        data = self.indexed_dataset()
        data_length = len(data)
        assert 0 <= index < data_length
        response = {}
        datas = []
        response['index'] = index
        for i in range(page_size):
            while True:
                curr = data.get(index)
                index += 1
                if curr is not None:
                    break
            datas.append(curr)

        response['data'] = datas
        response['page_size'] = len(datas)
        if data.get(index):
            response['next_index'] = index
        else:
            response['next_index'] = None
        return response
