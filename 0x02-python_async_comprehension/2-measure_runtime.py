#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four times
    """
    start = perf_counter()
    arr = []
    for _ in range(4):
        arr.append(async_comprehension())

    await asyncio.gather(*arr)

    times = perf_counter() - start
    return times
