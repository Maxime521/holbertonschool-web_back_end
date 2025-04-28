#!/usr/bin/env python3

"""Module for async_generator function"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous coroutine that generates 10 random numbers between 0 and 10,
    waiting 1 second between each generation.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
