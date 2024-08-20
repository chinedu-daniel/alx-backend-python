#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    coroutine that will execute async_comprehension four times
    """
    start_time = time.perf_counter()
    await async_function()
    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.4f} seconds")
