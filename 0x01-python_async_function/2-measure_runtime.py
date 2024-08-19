#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time 
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start
    return total / n
