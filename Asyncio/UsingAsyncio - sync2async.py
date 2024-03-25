import asyncio

# 定义一个协程函数，模拟异步操作
async def async_operation():
    print("Async operation started")
    await asyncio.sleep(2)  # 模拟异步操作，等待 2 秒
    print("Async operation completed")
    return "Result from async operation"

# 定义一个同步函数，用于处理异步事件
def sync_handler():
    # 使用 asyncio.run 来运行异步事件，并等待结果
    result = asyncio.run(async_operation())
    print("Sync handler got result:", result)


if __name__ == "__main__":
    # 调用同步函数来处理异步事件
    sync_handler()
    print("after Sync handler")
