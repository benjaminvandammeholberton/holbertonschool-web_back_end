#!/usr/bin/env python3
"Task 0 - The basics of async"

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    coroutine that waits for a random delay between 0 and max_delayseconds and
    eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
