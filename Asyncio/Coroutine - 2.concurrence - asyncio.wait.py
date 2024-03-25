# 协程函数
import asyncio


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    ret = 'Done after {}s'.format(x)
    print(ret)
    return ret

# 协程对象
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(3)

# 将协程转成task，并组成list
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  # asyncio.wait(tasks)确保了所有的task都被执行，但它不负责处理协程函数的返回值。
print('All done')
