import asyncio
import threading

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def async_task():
    while True:
        print("Hello, ")
        await asyncio.sleep(1)
        print("asyncio")
        await asyncio.sleep(1)


# 在新线程中启动事件循环
new_loop = asyncio.new_event_loop()
t = threading.Thread(target=start_loop, args=(new_loop,))
t.start()

# 在新的事件循环中安排任务
asyncio.run_coroutine_threadsafe(async_task(), new_loop)
