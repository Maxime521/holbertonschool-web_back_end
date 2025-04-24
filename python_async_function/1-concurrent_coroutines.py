#!/usr/bin/env python3

""" take in an integer and a max_delay integer as arguments"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int) -> float:
    """ waits for a random delay and returns the delay time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ takes in an integer and a max_delay integer as arguments"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
