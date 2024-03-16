from multiprocessing import Process, Pipe
def f(conn):

    # 子进程发送父进程端
    conn.send([42, None, 'hello from child'])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':

    # 生成管道实例。
    # 生成两个管道对象：parent_conn主，child_conn子
    parent_conn, child_conn = Pipe()

    # 生成主进程 args=连接对象
    p = Process(target=f, args=(child_conn,))
    p.start()

    # 接收子进程端
    print(parent_conn.recv())
    parent_conn.send("parent_conn.send")
    p.join()
