#!/usr/bin/env python3
"""
Module for async_generator function
"""
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float values asynchronously from async_generator.

    Returns:
        List[float]: 10 floats from async generator.
    """
    return [value async for value in async_generator()]
