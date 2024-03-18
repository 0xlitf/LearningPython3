import threading
import time

class ThreadWrapper(threading.Thread):
    def __init__(self):
        super().__init__()
        self.pause_event = threading.Event()
        self.stop_event = threading.Event()

    def thread_function(self):
        while not self.stop_event.is_set():
            self.pause_event.wait()  # 如果事件被清除（clear），线程将被阻塞
            print("Thread is running")
            time.sleep(1)

    def test(self):
        # 设置事件，使线程运行
        self.pause_event.set()

        # 创建并启动线程
        t = threading.Thread(target=self.thread_function)
        t.start()

        # 暂停线程
        time.sleep(2)
        print("Pausing thread")
        self.pause_event.clear()

        # 继续线程的执行
        time.sleep(2)
        print("Resuming thread")
        self.pause_event.set()

        time.sleep(2)
        print("stop thread")
        self.stop_event.set()


if __name__ == '__main__':
    t = ThreadWrapper()
    t.test()


    def thread_function():
        while True:
            print("Thread is running")
            time.sleep(1)

    t = threading.Thread(target=thread_function)
    t.start()
