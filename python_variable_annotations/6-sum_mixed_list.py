#!/usr/bin/env python3

""" Module to sum a list of integers and floats. """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return the sum a list of integers and floats """
    return sum(mxd_lst)
