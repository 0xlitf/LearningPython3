from threading import Thread

def multi_thread_shared_global_vars():
    list_a = [1, 2, 3]

    def add_list():
        global list_a
        list_a.append(100)
        print(list_a)

    t1 = Thread(target=add_list)
    t2 = Thread(target=add_list)
    print(t1.name)
    t1.start()
    print(t2.name)
    t2.start()


if __name__ == '__main__':
    multi_thread_shared_global_vars()
