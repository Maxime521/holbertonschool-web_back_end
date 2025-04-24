#!/usr/bin/env python3

"""
This module manages asyncio tasks and returns a sorted list of delays.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates multiple asyncio tasks, waits for their execution,
    and returns a sorted list of deadlines."""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
