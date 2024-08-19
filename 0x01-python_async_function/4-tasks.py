#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    alter it into a new function task_wait_n
    """
    runs = [task_wait_random(max_delay) for _ in range(n)]
    return [await con for con in asyncio.as_completed(runs)]
