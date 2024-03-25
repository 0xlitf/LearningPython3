import asyncio
import time

start = time.time()


async def func(delay):
    print("开始执行...")
    await asyncio.sleep(delay)  # 是一个异步等待的操作，而不是同步阻塞的操作
    print("结束执行...")


async def main():
    tasks = [
        asyncio.create_task((func(2))),
        asyncio.create_task((func(3)))
    ]
    # await asyncio.gather(*tasks)  # *tasks参数解包等同于 await asyncio.gather(task1, task2, task3)

asyncio.run(main())
print(abs(time.time() - start))

# await asyncio.wait(tasks)
# await不能在函数外调用，会报语法错误 SyntaxError: 'await' outside function
# 因为此时tasks没在协程函数内 故并没注册到事件循环对象中去
# await+ 可等待对象(协程对象、Future、Task-->I/O等待)  此时tasks不是可等待对象也不是协程对象
