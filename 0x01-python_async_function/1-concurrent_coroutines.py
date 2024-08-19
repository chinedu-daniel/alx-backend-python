#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n should return the list of all the delays
    """
    arr = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        arr.append(task)
    return [await r for r in ayncio.as_completed(arr)]
