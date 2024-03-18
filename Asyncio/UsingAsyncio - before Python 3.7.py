import asyncio

# 获取当前事件循环
loop = asyncio.get_event_loop()


# 定义一个简单的协程
async def hello_world():
    i = 0
    while i < 2:
        print("Hello, ")
        await asyncio.sleep(1)
        print("asyncio")
        await asyncio.sleep(1)
        i += 1

if __name__ == "__main__":
    # 在事件循环上运行协程直到完成
    loop.run_until_complete(hello_world())

    # 关闭事件循环
    loop.close()
