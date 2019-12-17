# 多进程，使用Process对象

from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p_1 = Process(target=f, args=('bob',))
    p_1.start()
    p_1.join()

    p_2 = Process(target=f, args=('alice',))
    p_2.start()
    p_2.join()