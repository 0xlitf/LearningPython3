import asyncio
import time


async def _sleep(x):
    time.sleep(x)
    return '暂停了{}秒！'.format(x)


coroutine = _sleep(2)
loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coroutine)


print('run_until_complete')
loop.run_until_complete(task)

# task.result() 可以取得返回结果
print('返回结果：{}'.format(task.result()))

import time
import asyncio


async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒！'.format(x)


def callback(future):
    print('callback，获取返回结果是：', future.result())


coroutine = _sleep(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

# 添加回调函数
print('add_done_callback')
task.add_done_callback(callback)

print('run_until_complete')
loop.run_until_complete(task)
