# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------------------
#      process and thread
#---------------------------------------------------------------------------------------------

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319272686365ec7ceaeca33428c914edf8f70cca383000

# One process has at least one thread.

###############################################################################
#     multiprocessing
###############################################################################

# multiprocessing

from multiprocessing import Process
import os

def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getpid()))
    
if __name__ == '__main__':
    print('run parent process %s' % os.getpid())
    p = Process(target = run_proc, args = ('test', ))
    print('child process will start')
    p.start()
    p.join()
    print('child process ends')
#%%
    
#  pool

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %0.2f seconds.' % (name, (end- start)))

if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Pool(4) # run 4 processes each time
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print('waiting for all subprocesses done...')
    p.close() # close is necessary before join
    p.join()
    print('all subprocesses done.')

# When running this in spyder, it keeps waiting like forever.

# It works in cmd.
# open cmd
# python D:\python\python\Note7-liao.py
# (you need to input the absolute path)
#%%

# subprocess

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
#%%

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
#%%

# communication between differente processes

from multiprocessing import Process, Queue
import os, time, random

# write
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# read
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate() # dead loop. need to terminate it.
#%%
    
###############################################################################
#               thread
###############################################################################

# two modules: _thread, threading
# Threading is the advanced one. 

import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#%%

# lock

import time, threading

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock() # only one thread can run the run_thread funciton

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

###############################################################################
#        thread local
###############################################################################

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
#%%

###############################################################################
#            distributed processes
###############################################################################

