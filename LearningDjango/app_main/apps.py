from django.apps import AppConfig
import threading
from .scheduled_tasks import ScheduledTasks
import asyncio

async def periodic_task(initial_delay, interval, func, *args, **kwargs):
    """执行定期异步任务，支持同步和异步函数"""
    await asyncio.sleep(initial_delay)  # 首次延迟
    while True:
        if asyncio.iscoroutinefunction(func):
            # 如果func是异步函数，使用await调用
            await func(*args, **kwargs)
        else:
            # 如果func是同步函数，使用run_in_executor来避免阻塞事件循环
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, func, *args, **kwargs)
        # 等待下一次执行
        await asyncio.sleep(interval)

# 示例使用
async def async_task(arg1, arg2):
    print(f"Async task executed with {arg1}, {arg2}")

def sync_task(arg1, arg2):
    print(f"Sync task executed with {arg1}, {arg2}")

async def main():
    # 启动异步任务
    asyncio.create_task(periodic_task(0, 1, async_task, "async_arg1", "async_arg2"))

    # 启动同步任务
    asyncio.create_task(periodic_task(0, 2, sync_task, "sync_arg1", "sync_arg2"))

    # 保持主程序运行，以便异步任务可以执行
    await asyncio.sleep(5)  # 示例：运行60秒后停止


import threading
import queue
import time


def producer(queue):
    for i in range(5):
        time.sleep(1)  # 模拟生产过程
        item = f"item {i}"
        print(f"Producing {item}")
        queue.put(item)


def consumer(queue):
    while True:
        item = queue.get()
        print(f"Consuming {item}")
        queue.task_done()  # 表示任务已完成
        time.sleep(2)


def communication_in_threads():
    q = queue.Queue()
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    q.join()  # 等待队列中的任务全部执行完成


# app的启动类
class app_main_config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_main'

    def ready(self):
        print('app_main_config ready!')

        # task = ScheduledTasks()

        # threading.Timer(1, task.scheduled_task_1).start()

        # asyncio.run(main())

        # communication_in_threads()

        