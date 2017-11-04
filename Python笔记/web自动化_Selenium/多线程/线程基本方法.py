import time, threading


def run_thread(n):
    print(n)
    print(threading.current_thread().name)


threads = []

t1 = threading.Thread(target=run_thread, args=(5,))
threads.append(t1)
t2 = threading.Thread(target=run_thread, args=(8,))
threads.append(t2)
# 如果用了join()，主线程运行到这里就会等待两个子线程t的运行
# 直到这两个线程运行完毕，才会继续只是主线程，也就是运行后面的print('end')
# 如果不加join(),主线程在运行所有代码后才会阻塞，等待两个子线程运行完毕
for t in threads:
    # t.setDaemon(False)
    t.start()
    t.join()
# t1.join()
# t2.join()
print('end')

"""
print_func（）中的while循环没有继续执行下去就退出了，
可见由于setDaemon(True)把子线程设置为守护线程，
子线程启动后，父线程也继续执行下去，
当父线程执行完最后一条语句print "end"后，没有等待子线程，直接就退出了，同时子线程也一同结束。
join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。，无法运行下去。
"""