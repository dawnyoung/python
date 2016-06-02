# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:04:29 2016

@author: Administrator
"""

#------------------------------------------------------------------------------------------------
#          bug, debug, test
#------------------------------------------------------------------------------------------------

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431913726557e5e43e1ee8d54ee486bddc3f607afb75000

###############################################################################
#   try...except...finally
###############################################################################

try:
    print('try....')
    r = 10 / 0
    print('try....')
    # if there is sth wrong, the following will not be excuted. 
    # skip to the except part
    # If there is no error, the except part will be skipped.
except ZeroDivisionError as s:
    print('except', s)
finally:
    print('finally')
print('end')

# There may be more than one error. So we can use more than one except.
#%%

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
#%%

# Using logging to record error information
import logging
logging.basicConfig(level = logging.info) # define the level of information
# debug
# info
# warning
# error

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)/2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('end')

# by logging, all the lines will be excuted even there is an error
# Error information can be saved in log
#%%

###############################################################################
#   debugging
###############################################################################

# Throw an error
class FooError(ValueError): # error is class
    pass

def foo2(s):
    n = int(s)
    if n==0: # when to throw error
        raise FooError('invalid value: %s' % s) # throw an error
    return 10 / n

foo2('0')
#%%

# print(): show the errors

# assert(): used to replace print()
def foo3(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    # n!=0 should be True. If not, error raised ('n is zero!')
    return 10 / n

def main():
    foo3('0')

main()
#%%

# pdb
# line by line

# pdb.set_trace()
import pdb

s = '0'
n = int(s)
pdb.set_trace() # pause automatically
print(10 / n)

# p n : show the variable n
# c: continue
#%%

###############################################################################
#   unit test
###############################################################################

