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

