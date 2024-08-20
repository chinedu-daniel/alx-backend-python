#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine called that takes no arguments.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
