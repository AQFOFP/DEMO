import threading

# 创建全局ThreadLocal对象
import time

local_school = threading.local()


class Student():
    def __init__(self, name):
        self.name = name


def process_student(name):
    std = Student(name)
    local_school.student = std   # 写操作
   # local_school.teacher = std
    do_task_1()
    time.sleep(5)
    do_task_2()


def do_task_1():
    std = local_school.student  # 读操作
    print("do_task_1", std.name)


def do_task_2():
    std = local_school.student   # 读操作
    print("do_task_2", std.name)


if __name__ == '__main__':
    '''
    全局变量local_school，每个线程对它都可以读写student属性，而且互不影响。可以把local_school看成是全局变量，
    但是每个属性如local_school.student都是线程的局部变量，可以任意读写互不干扰，也不用管理锁的问题
    
    一个threading.local变量虽然是全局变量，但是每个线程都只读写自己线程的独立副本，互不干扰。
    threading.local解决了参数在一个线程中各个函数之间互相传递的问题
    '''

    t1 = threading.Thread(target=process_student, args=("Curry",))
    t2 = threading.Thread(target=process_student, args=("大雄",))
    t1.start()
    t2.start()