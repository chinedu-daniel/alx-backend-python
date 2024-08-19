#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n should return the list of all the delays
    """
    spawn = []
    delay = []

    for _ in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lamba x: delay.append(x.result()))
        spawn.append(delayed_task)

        #wait for all tasks to complete
        await asyncio.gather(*spawn)

        #Return delays in ascending order
        return sorted(delay)

