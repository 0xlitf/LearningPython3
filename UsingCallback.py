# coding=utf-8

def usage_1():
    def callback_function(result):
        print(f"Callback received result: {result}")

    def main_function1(callback):
        # 模拟一些操作
        result = "some result"
        # 调用回调函数
        callback(result)

    main_function1(callback_function)

def usage_2():
    def main_function2(callback):
        # 模拟一些操作
        result = "some result"
        # 调用回调函数
        callback(result)


    # 使用lambda作为回调
    main_function2(lambda result: print(f"Callback received result: {result}"))


def usage_3():
    class CallbackHandler:
        def __init__(self, initial_data):
            self.data = initial_data

        def callback(self, result):
            self.data += result
            print(f"Updated data: {self.data}")

    def main_function3(callback):
        # 模拟一些操作
        result = " appended result"
        # 调用回调函数
        callback(result)

    handler = CallbackHandler("Initial data")
    # 使用类的方法作为回调
    main_function3(handler.callback)


# 使用回调

if __name__ == '__main__':
    usage_1()
    usage_2()
    usage_3()
