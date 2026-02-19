from typing import Coroutine
import asyncio

def deco(coroutine: Coroutine):
    async def wrapper(*args, **kwargs): # такое же объявление как у целевой функиции
        res = await coroutine(*args, **kwargs)
        return res
    return wrapper

@deco
async def my_async_func():
    await asyncio.sleep(2)
    print("Async Magic")
    return 1

asyncio.run(my_async_func())
#my_async_func = deco(my_async_func)

