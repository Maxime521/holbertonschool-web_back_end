#!/usr/bin/env python3

""" Type annotation for to_kv function """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return the sum a list of integers and floats """
    return (k, float(v ** 2))
