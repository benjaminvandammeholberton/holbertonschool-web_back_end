#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that spawns wait_random n times with the specified max_delay
    Returns the list of all the delays
    """
    results: list = await asyncio.gather(*(wait_random(max_delay)
                                           for _ in range(n)))
    sorted_result: list = sorted(results)
    return sorted_result
