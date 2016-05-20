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

# An object includes data and function

###############################################################################
#   Class and Instance
###############################################################################

# create a class named Student
class Student(object):
    pass

# create a instance under this class
cart = Student()

print(Student)
print(cart)

# add proporty to this instance
cart.name = "Cart Bing"
print(cart.name)
#%%

# create and add proporties to a class
class Student2(object):
    def __init__(self, name, score): # the first parameter is always self
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'D'

# If the proporties are defined in the class, the parameter cannot be empty when
# create a new instance
cart = Student2('Cart Bing', 80)
print('cart is ', cart)
print('name is ', cart.name)
print('score is ', cart.score)
cart.print_score()
cart.get_grade()
#%%

###############################################################################
#  Access ristrictions
###############################################################################

# private

class Student3(object):
    def __init__(self, name, score):
        self.__name = name # set name as private variable
        self.__score = score # set score as private variable
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name
        
    def get_score(self):
        return self.__score
        
    def set_score(self, score):
        self.__score = score
        

kobe = Student3('kobe', 20)
#print(kobe.__name) # name cannot be called directly

# get name and score by the defined function get_name and get_score
print(kobe.get_name())
print(kobe.get_score())

kobe.set_score(40) # change the data
kobe.get_score()
#%%

###############################################################################
#   Subclass
###############################################################################

# base class, super class -> subclass

class Animal(object): # base class (super class) of Dog and Cat
    def run(self):
        print('Animal is running')
        
class Dog(Animal): # Dog is subclass of animal
    pass

class Cat(Animal): # Cat is subclass of animal
    pass
# subclass gets every function in base class
#%%

# add function to subclass
class Dog2(Animal):
    def run(self):# The same function. Subclass overlaps base class
        print('Dog is running')
#%%
        
###############################################################################
# Get information of an object
###############################################################################
        
type(123) # return what class this belongs
type(1) == type(2) #True
type(kobe) #class: Student3
#%%

isinstance(123, int)
isinstance('123', str)

print(isinstance((1,2,3), (list, tuple))) # if it is a list or a tuple
#%%

dir(1) # return every proporty and function 
#%%

print(hasattr(kobe, 'get_name')) # Dose kobe has attribute named get_name?
print(hasattr(kobe, 'name')) # name is private

print(hasattr(kobe, 'height'))
setattr(kobe, 'height', 6) # set a new attribute height
print(hasattr(kobe, 'height'))
#%%

h = getattr(kobe, 'height') # give the attr of kobe to h
h
#%%

del kobe.height # delete attr
print(hasattr(kobe, 'height'))
#%%

