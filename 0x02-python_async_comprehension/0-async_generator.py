#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """
    Async generator that yields a random number between 0 and 10,
    10 times with 1 second delay each time.
    """
    for i in range(10):   # Loop 10 times
        await asyncio.sleep(1)  # Asynchronously wait 1 second

        # Gives a random number between 0 and 10
        yield random.randint(0, 10)
