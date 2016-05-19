# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:01:00 2016

@author: Administrator
"""

#----------------------------------------------------------------------------------------------
#        Modules
#----------------------------------------------------------------------------------------------
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318447437605e90206e261744c08630a836851f5183000

#!/usr/bin/env python3 
# (make this can be execute on Unix/Linux/Mac)

# -*- coding: utf-8 -*-
# (using utf-8 code)

'a test module' #the first string will be treated as comments to this module

__author__ = 'Dawn' # the name of author

import sys # import necessary module

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print('Hellow %s', args[1])
    else:
        print('too many arguments')

if __name__ == '__main__':
    test()
#%%

def _private_1(name): # private variable, which cannot be used outside this module
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name): # public variable, which can be called from outside this module
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
#%%

#----------------------------------------------------------------------------------------------
#      Object Oriented Programming
#----------------------------------------------------------------------------------------------

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000

