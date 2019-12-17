# coding:utf-8
import asyncio

# 通过create_task()方法
async def a(t):
    print('-->', t)
    await asyncio.sleep(0.5)
    print('<--', t)
    return t * 10

async def b():
    # loop = asyncio.get_event_loop()
    cnt = 0
    while True:
        cnt += 1
        cor = a(cnt)   # coroutine
        resp = loop.create_task(cor)
        await asyncio.sleep(0.1)
        # print(resp)

loop = asyncio.get_event_loop()

loop.run_until_complete(b())
