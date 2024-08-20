#!/usr/bin/env python3
"""
Async Comprehensions
"""
import asyncio
from typing import List
async_generator = __import__('0_async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async comprehensing
    """
    return [item async for item in async_generator()]
