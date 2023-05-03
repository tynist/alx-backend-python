#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time it takes to execute async_comprehension 4 times
    in parallel using asyncio.gather().

    Returns:
        float: the total runtime in seconds.
    """
    starts_time = time.perf_counter()
    # run async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    ends_time = time.perf_counter()
    return ends_time - starts_time

