#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio
import time 


async def async_generator():
    """
    A coroutine called that takes no arguments.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield i
