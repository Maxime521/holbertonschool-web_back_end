#!/usr/bin/env python3

"""Module for async_generator function"""

import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields a random number between 0 and 10
    after asynchronously waiting for 1 second, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
