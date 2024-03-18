import asyncio


async def task_1():
    i = 0
    while True:
        print(f"1. Hello, {i}")
        await asyncio.sleep(1.1)
        print(f"1. asyncio {i}")
        await asyncio.sleep(1.2)
        i += 1
        c["a"] = i

async def task_2():
    i = 0
    while True:
        print(f"2. Hello, {i}")
        await asyncio.sleep(1.3)
        print(f"2. asyncio {i}")
        await asyncio.sleep(1.4)
        i += 1
        c["b"] = i

c = {"a": 0, "b": 0}


async def task_print():
    while True:
        print(f"c: {c}")
        await asyncio.sleep(3)


async def main():
    # 使用 asyncio.gather 同时运行三个任务
    await asyncio.gather(
        task_1(),
        task_2(),
        task_print(),
    )

if __name__ == "__main__":
    asyncio.run(main())