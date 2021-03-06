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
        
# unit test
import unittest

from mydict import Dict

class TestDict(unittest.TestCase): # base class: unittest.TestCase
    def test_init(self): # test starts with test
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
    def setUp(self): # excute before each unit
        print('before excuting the unit')
    def tearDown(self): # excute after each unit
        print('after excuting the unit')
    # For example, we can use setUp to open a database, and use tearDown to close
    # a database. The setUp and tearDown will be excuted before or after each unit.
    # It makes it unnecessary to write the open and close code in each unit.

if __name__ == '__main__':
    unittest.main()
#%%

###############################################################################
#         doctest
###############################################################################
class Dict2(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict2()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict2(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict2' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict2' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
#%%