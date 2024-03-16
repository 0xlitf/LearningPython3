from multiprocessing import Process, Manager
import os


def f(d, l):
    # 存入每个进程PID到字典
    d[os.getpid()] = os.getpid()

    # 每个进程放入进程ID
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':

    # Manager() 赋值变量为 manager
    with Manager() as manager:

        # 生成一个字典.dict()，可在多个进程传递共享的字典
        d = manager.dict()

        # 生成一个列表.list()，可在多个进程传递共享的列表
        l = manager.list()
        p_list = []
        for i in range(10):
            # 生成10个进程，args=(字典，列表)
            p = Process(target=f, args=(d, l))

            # 执行进程
            p.start()

            # 对象存放在空的列表内
            p_list.append(p)

        # 等待结果
        for res in p_list:
            res.join()

        print(d)
        print(l)
