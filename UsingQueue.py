from multiprocessing import Process, Queue


def f(q):
    # 主进程传入数据
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    # 实例化进程queue
    q = Queue()

    # 实例一个子进程，调用f，args=获取q.put克隆数据
    p = Process(target=f, args=(q,))

    # 执行进程
    p.start()

    # 获取数据
    print(q.get())

    # 等待进程执行完
    p.join()
