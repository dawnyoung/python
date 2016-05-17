# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:13:36 2016

@author: Administrator
"""

# basic information

#list

names = ['bob', 'penny', 'kate'];
names[0]
names[1]
names[2]
#index starts from 0, end at len(list)-1

#another way to print the last element in a list
print(names[-1])
print(names[-2])

#delete an element at a specific position
print('delete an element')
names.pop(2)
print(names)

#insert an element
print('insert an element')
names.insert(1, 'penny')
print(names)

#replace
print('replace an elment')
names[1] = 'john'
print(names[1])

#the element of a list can be a list
#%%


#  tuple

#similar to list. but cannot be changed

names2 = ('bob', 'penny', 'kate')

#if there is only one element, we need to add a , at the end of this element
names3 = ('bob',)


#if there is a list in tuple, the element in list can be chagned
print('before changing')
names4 = ('bob', 'penny', ['boy', 'girl'])
print(names4)

print('after changing')
names4[2][0] = 'unknown'
print(names4)
#%%


######################################################################
#  conditional argument                                            ###
######################################################################

#if
age = 20
if age > 18:
    print ("your age is", age)
    print ('adult')
elif age > 12:
    print ('your age is', age)
    print ('youth')
else:
    print ('your age is ', age)
    print ('child')
#%%
    

#for
names = ['nida', 'jay', 'sam']
for name in names:
    print (name)

#calculate the sum of numbers from to 100
s = 0 
for x in range(101):#range(101): 0 - 100, 101 numbers in total. begins from 0!
    s = s +x
    print (s)


# ctrl + c: quit present command
#%%



##########################################################################
#            dict and set                                                #
##########################################################################

#dict
d = {'nida': 100, 'jay': 90, 'sam': 80}
d['nida']

d['rose'] = 70

#set
s = set([1,2,3])
s2 = set([1,2,2,3,4,5])
s2 #values in set cannot repeat

#add value into a set:  add(key)
s.add(4)
s
#remove value from a set: remove(key)
s.remove(4)
s

s & s2 #intersection
s | s2 #union
#%%



###########################################################################
#            define a function                                         ###
###########################################################################


def my_abs(x):
    if not isinstance(x, (float, int)):
        raise TypeError ('bad operand type') 
        #if input is not floar or int, then report error
    if x > 0:
        return x
    else:
        return -x
#%%
  
        
def power(x, n = 2):
    s = 1
    while n >0 :
        n = n-1
        s = s* x
    return s


power(5)#5^2 by default
power(5, 3)

# parameters by default should be after the other parameters.
# For example, x has no default value while n is 2 by default. We need to put x
# before n.

# There can be more than one parameters by default. 
#%%


# Stationary parameter
# The number of input values cannot be changed
def calc(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum
# If more than one input, we need use tuple or list as input (put all the inputs together)
print(calc((1, 2, 3)))
print(calc([1,3]))
print(calc([1]))

# Variable parameter
def calc2(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum
# It works no matter how many inputs we have
print(calc2(2,3))
print(calc2(1))

print('when use list or tuple as input')
numbers = [1,2,3]
print(calc2(*numbers))
#%%

# Key word parameter
# Key word parameter can use dict as input
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('a', 2))
print(person('b', 3, city = 'chicago'))
#%%


###########################
#   recursive function
###########################

# a function calls itself

# Factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(3))
#%%

# Use tail recersion to minimize the effect of stack overflow

# no expression in return

def fact2(n):
    return fact3(n, 1)

def fact3(n, f):
    if n == 1:
        return f
    return fact3(n - 1, n * f)

print(fact2(3))
print(fact3(3, 1))
#%%