#!/usr/bin/env python3
"""
Module for measuring runtime of async operations
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension 4 times in parallel
    Returns: total runtime in seconds (approximately 10 seconds)
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
