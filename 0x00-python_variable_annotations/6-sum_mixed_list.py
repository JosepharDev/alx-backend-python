#!/usr/bin/env python3
""" write a type annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list if integers and floats and return their sum as float """
    tmp: float = 0.0
    for i in mxd_lst:
        tmp += i
    return tmp
