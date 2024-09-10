import threading

condition_a = threading.Condition()
condition_b = threading.Condition()
a_ready = False
b_ready = False

def thread_a():
    global b_ready
    print('a线程开始执行')
    with condition_a:
        while not a_ready:
            condition_a.wait()
    # 执行 A 线程的操作
    with condition_b:
        b_ready = True
        condition_b.notify()

def thread_b():
    global a_ready
    # 执行 B 线程的初始操作
    print('b线程开始执行')
    # 执行 B 线程后续操作
    with condition_a:
        a_ready = True
        condition_a.notify()
    with condition_b:
        while not b_ready:
            condition_b.wait()


t1 = threading.Thread(target=thread_a)
t2 = threading.Thread(target=thread_b)

t1.start()
t2.start()

t1.join()
t2.join()