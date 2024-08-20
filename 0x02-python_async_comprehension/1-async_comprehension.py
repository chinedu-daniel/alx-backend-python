#!/usr/bin/env python3
"""
Async Comprehensions
"""
import asyncio
import random
async_comprehension = __import__('0_async_generator').async_comprehension


async def async_comprehension():
    """
    collect 10 random numbers using an async comprehensing
    """
    return [item async for item in async_generator()]
