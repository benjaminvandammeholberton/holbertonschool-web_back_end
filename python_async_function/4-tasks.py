#!/usr/bin/env python3
"Tasks"

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that spawns wait_random n times with the specified max_delay
    Returns the list of all the delays
    """
    results: list = await asyncio.gather(*(task_wait_random(max_delay)
                                           for _ in range(n)))
    sorted_result: list = sorted(results)
    return sorted_result
