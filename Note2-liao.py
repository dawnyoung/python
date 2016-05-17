# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:52:37 2016

@author: Administrator
"""

# ---------------------------------------------------------------------------------------------------------
#            Advance properties
# ---------------------------------------------------------------------------------------------------------
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868196169906eb9ca5864384546bf3405ae6a172b3e000


################################################################################
#       slice
################################################################################

l = range(50)

# the first 10 numbers in l
print(l[:9])

# the last 10 numbers in l
print(l[-9:])

l[::5] # from 0 to 50, common difference is 5

l[10:20:3] # from 11 to 21, common difference is 3
#%%

'abcdef'[:3]
#%%

(1,2,3,4)[-3:-1]
#%%

################################################################################
# iteration
################################################################################

# Iteration can be used for list, tuple, dict

# For-loop

print('iteration for keys in dict')
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

print('iteration for values in dict')
for value in d.values():
    print(value)

print('iteration for both keys and values')
for k, v in d.items():
    print(k,v)
#%%

# How to check if an object is iterable

from collections import Iterable
isinstance ('abc', Iterable)
#%%

for i, value in enumerate(['a', 'b']): #enumerate turns list into index-element pair
    print(i, value)
#%%

###############################################################################
# list comprehensions
###############################################################################

"[1,2,3,4,5,6,7,8,9,10"
range(1, 11)
#%%

"[1*1, 2*2, 3*3]"
[x*x for x in range(1,4)]
#%%

# square of even numbers
[x*x for x in range(1, 11) if x % 2 == 0]
#%%

[m+n for m in "abc" for n in 'def']
#%%

l = ['a', 'b']
[s.upper() for s in l] # turn lower case into upper case
#%%

###############################################################################
# generator
###############################################################################

# change [] into ()
l = [x*x for x in range(10)] # list
g = (x*x for x in range(10)) # generator

# print the elements in this generator one by one
# Generator is iterable
for n in g:
    print(n)
#%%

# Fibonacci

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print (b)
        a, b = b, a+b
        n = n + 1

fib(6)
#%%

# use generator to obtain Fibonacci

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b) # change print to yield to make it a generator
        a, b = b, a+b
        n = n+1
fib(6)
#%%