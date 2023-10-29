import asyncio
import contextvars
import functools
import time


async def to_thread(func, /, *args, **kwargs):
    loop = asyncio.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)


# a blocking io-bound task
def blocking_task():
    # report a message
    print('Task starting')
    # block for a while
    time.sleep(2)
    # report a message
    print('Task done')


# main coroutine
async def main():
    # report a message
    print('Main running the blocking task')
    # create a coroutine for  the blocking task
    coro = to_thread(blocking_task)
    # schedule the task
    task = asyncio.create_task(coro)
    # report a message
    print('Main doing other things')
    # allow the scheduled task to start
    await asyncio.sleep(0)
    # await the task
    await task


# run the asyncio program
asyncio.run(main())
