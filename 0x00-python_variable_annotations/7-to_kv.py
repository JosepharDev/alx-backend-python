#!/usr/bin/env python3
""" write a type annotated function to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple of string and float """
    tmp = v ** 2
    return (k, tmp)
