#!/usr/bin/env python3
" Async Generator"

import asyncio
import random
from typing import AsyncGenerator


async def  async_generator() -> AsyncGenerator[float, None]:
    for i in range(0, 11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
