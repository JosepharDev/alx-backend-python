#!/usr/bin/env python3

""" write a type annotated function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list of floats and return sum as float """
    tmp: float = 0.0
    for i in input_list:
        tmp += i
    return tmp
