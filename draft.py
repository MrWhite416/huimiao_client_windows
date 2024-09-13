import asyncio
import datetime
import threading

c_a = asyncio.Condition()
c_b = asyncio.Condition()


async def a():
    print('a协程被执行', datetime.datetime.now())
    print('aaaaaaaaaaa')
    async with c_a:
        await c_a.wait()
    print('a协程执行完毕')


async def b():
    print('b协程被执行', datetime.datetime.now())
    await asyncio.sleep(0.5)  # 添加一些延迟
    print('bbbbbbbbbbbb')
    async with c_a:
        c_a.notify()
    print('b协程执行完毕')


async def r():
    a_s = asyncio.create_task(a())
    b_s = asyncio.create_task(b())
    await asyncio.gather(a_s, b_s)


asyncio.run(r())
