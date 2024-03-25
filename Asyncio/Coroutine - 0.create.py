
from collections.abc import Coroutine


async def hello(name):
    print('Hello,', name)


if __name__ == '__main__':
    # 生成协程对象，并不会运行函数内的代码
    coroutine = hello("World")

    # 检查是否是协程 Coroutine 类型
    print(isinstance(coroutine, Coroutine))  # True

import asyncio
from collections.abc import Generator, Coroutine

'''
只要在一个生成器函数头部用上 @asyncio.coroutine 装饰器
就能将这个函数对象，【标记】为协程对象。注意这里是【标记】，划重点。
实际上，它的本质还是一个生成器。
标记后，它实际上已经可以当成协程使用。后面会介绍。
'''


@asyncio.coroutine  # 报警告 DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
def hello():
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)


if __name__ == '__main__':
    coroutine = hello()
    print(isinstance(coroutine, Generator))  # True
    print(isinstance(coroutine, Coroutine))  # False


    # 2. asyncio的几个概念
    # 在了解asyncio的使用方法前，首先有必要先介绍一下，这几个贯穿始终的概念。
    # event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    # coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
    # future 对象： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
    # task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。
    # async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。
    # 这几个概念，干看可能很难以理解，没事，往下看实例，然后再回来，我相信你一定能够理解。

    # 协程完整的工作流程是这样的 - 定义/创建协程对象 - 将协程转为task任务 - 定义事件循环对象容器 - 将task任务扔进事件循环对象中触发
    import asyncio


    async def hello1(name):
        print('Hello,', name)


    # 定义协程对象
    coroutine1 = hello1("World")

    # 定义事件循环对象容器
    loop1 = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine)

    # 将协程转为task任务
    task1 = loop1.create_task(coroutine1)

    # 将task任务扔进事件循环对象中并触发
    loop1.run_until_complete(task1)


    # 4. await与yield对比
    # 前面我们说，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。
    # 注意这里是，一定程度上，意思是效果上一样（都能实现暂停的效果），但是功能上却不兼容。就是你不能在生成器中使用await，也不能在async 定义的协程中使用yield from。
    # 小明不是胡说八道的。有实锤。 普通函数中 不能使用 await 再来一锤。 async 中 不能使用yield
    # 除此之外呢，还有一点很重要的。
    # yield from 后面可接 可迭代对象，也可接future对象/协程对象；
    # await 后面必须要接 future对象/协程对象

# yield from 后面可接 可迭代对象，这个前两章已经说过了，这里不再赘述。 接下来，就只要验证，yield from和await都可以接future对象/协程对象就可以了。
#
# 验证之前呢，要先介绍一下这个函数： asyncio.sleep(n)，这货是asyncio自带的工具函数，他可以模拟IO阻塞，他返回的是一个协程对象。
    func = asyncio.sleep(2)
    from asyncio.futures import Future
    print("isinstance(func, Future) ", isinstance(func, Future))  # False
    print("isinstance(func, Coroutine) ", isinstance(func, Coroutine))  # True

# 还有，要学习如何创建Future对象，不然怎么验证。 前面概念里说过，Task是Future的子类，这么说，我们只要创建一个task对象即可。

    import asyncio
    from asyncio.futures import Future


    async def hello2(name):
        await asyncio.sleep(2)
        print('Hello, ', name)


    coroutine2 = hello2("World")

    # 将协程转为task对象
    task2 = asyncio.ensure_future(coroutine2)

    print("isinstance(task, Future) ", isinstance(task2, Future))  # True
