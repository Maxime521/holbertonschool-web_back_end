#!/usr/bin/env python3

""" Module for element_length function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    def multiply(number: float) -> float:
        """ returns the product of the number and multiplier """
        return number * multiplier
    return multiply
