#!/usr/bin/env python3
"Run time for four parallel comprehensions"

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes "async_comprehension" four times in parallel
    using "asyncio.gather"
    """
    tasks = [asyncio.create_task(async_comprehension()) for i in range (0, 4)]
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start
