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

# ----------------------------------------------------------------------------------------------
# Functional programming
#-----------------------------------------------------------------------------------------------
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819866394c3f9efcd1a454b2a8c57933e976445c0000


###############################################################################
# Higher order function
###############################################################################

###################   map() &  reduce()

# map(function, list)
# works on each element in the list respectively
def f(x):
    return x*x
list(map(f, [1,2,3,4])) # put the result of map into a list
#%%

tuple(map(str, range(10))) # put the result of map into a tuple
#%%


# reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# accumulative effect
from functools import reduce
def add(x, y):
    return x+y
reduce(add, [1,2,3])
#%%

def product(x, y):
    return x*y
reduce(product, [1,2,3,4])
#%%

# normal form of names

def name(x):
    x = x.lower() #change every character into lower case
    return x.capitalize() #capitalize the initials
list(map(name, ['adam', 'LISA', 'barT']))
#%%
from functools import reduce
def prod(x, y):
    return x*y
reduce(prod, [1,2,3])
#%%

################################# filter(function, list)

# keep or remove the elements in list according to the return of this funciton (true or false)

# keep odd numbers
def is_odd(x):
    return x % 2 == 1 # remainder is 1
list(filter(is_odd, [1,2,3,4,5]))
#%%

# remove the prime between 1 and 100
import math
def deleteprime(x):
    flag = 0
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            flag = 1
    if flag == 1:
        return x
list(filter(deleteprime, range(1, 101)))
#%%

# remove empty element
def not_empty(x):
    return x and x.strip()
# The method strip() returns a copy of the string in which all chars have been 
# stripped from the beginning and the end of the string (default whitespace characters).
# strip only removes the beginning and the end
list(filter(not_empty, ['a', '', 'c']))
#%%

############################  sorted()

print(sorted([1,3,5,2,-3]))

print(sorted([1,3,5,2,-3], key = abs)) # sort for absolute value

# descending order
print(sorted([1,3,5,2,-3], key = abs, reverse = True))
#%%

l = ['Z', 'a', 'B']

# upper case is before lower case based on ASCII
print(sorted(l))

# ignore upper case or lower case
print(sorted(['Z', 'a', 'B'], key = str.lower))
#%%

# names and scores for 4 students
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#sorted by name
print(sorted(l, key = lambda l2:l2[0]))

# sorted by scores
print(sorted(l, key = lambda l2:l2[1], reverse = True))
#%%

###############################################################################
# return function
###############################################################################

# Closure
# A function returns a function. 
# Parameters and variables are saved in the returned fucntion.

def lazy_sum(*x):
    def mysum():
        ms = 0
        for i in x:
            ms = ms + i
        return ms
    return mysum

print(lazy_sum(1,2,3,4)) #return a function

f = lazy_sum(1,2,3,4)
print(f) # return a function
"the function will be executed when f is called"
print(f())

f2 = lazy_sum(1,2,3,4)
print(f == f2) # f is different from f2 even with the same function and same input
#%%

###############################################################################
#  lambda
###############################################################################

list(map(lambda x:x*x, [1,2,3]))
#%%

# lambda can be used as returned value
def sumofsquare(x, y):
    return lambda: x*x + y*y
print(sumofsquare(1,2)) # return a fucntion

f = lambda x, y: x*x + y*y
print(f) # f is a function
#%%

###############################################################################
# decorator
###############################################################################

