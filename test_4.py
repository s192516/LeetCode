#-*- coding:utf-8 -*-
#@Date   : 2018/12/16
#@Author : suyifan
#@File   : test_4.py



import time
import os
from multiprocessing import Process


def long_time_task(i):
    print("当前进程{},任务{}".format(os.getpid(),i))
    time.sleep(2)

if __name__ == "__main__":
    print("当前母进程{}".format(os.getpid()))
    start = time.time()
    for i in range(15):
        # long_time_task(1)
        p1 = Process(target=long_time_task,args=(i,))
        # print("等待所有子进程结束")
        p1.start()
    p1.join()

    # p2 = Process(target=long_time_task,args=(2,))
    # p2.start()
    # p2.join()
    end = time.time()
    print("用时{}秒".format((end - start)))



