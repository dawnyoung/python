# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:35:04 2016

@author: Administrator
"""

#----------------------------------------------------------------------------------------------
#   Advanced Object Oriented Programming
#----------------------------------------------------------------------------------------------

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000

###############################################################################
#   __slots__
###############################################################################

class Student(object):
    __slots__ = ('name', 'age') # only these two properties can be added 

s = Student()
s.name = 'kobe' # works
s.age = 34 # works
s.score = 84
# this will return an error
# AttributeError: 'Student' object has no attribute 'score'
# because we use __slots__ to limit what proporties can be added
#%%

class GradStudent(Student):
    pass

gs = GradStudent()
gs.score = 80 # no error returned
# __slots__ only works on the present instance/class
# it does not limit the sub class
#%%

###############################################################################
#                 @property
###############################################################################

class Student2(object):
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must be between 0~100!')
        self.score = value
    # setter is defined. This is not read only
    
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
        
    @property
    def age(self):
        return 2016 - self._birth
    # no setter defined for age
    # age is read only
#%%

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    
    @property # read only
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
#%%

###############################################################################
#         multiple inheritance
###############################################################################

# Mixin

class Animal(object):
    pass

class Mammal(Animal):
    pass
class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('runnint')
class Flyable(object):
    def fly(self):
        print('flying')

class Bat(Mammal, Flyable): # multiple inheritance
    pass
class Dog(Mammal, Runnable): # multiple inheritance
    pass
#%%
    
###############################################################################
#   __XX__
###############################################################################
    
# __str__
# return a string as you like
class Student3(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student3('kobe'))
Student3('kobe') # return <__main__.Student3 at 0x78f7990>
# because without print, it uses __repr__
# to solve this problem, define a __repr__
#%%

class Student4(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'student object(name: %s)' % self.name
    __repr__ = __str__
    # generally, __repr__ is the same with __str__

Student4('kobe')
#%%

# __iter__
# Fib works like a list, which can be used for iteration
# However, we cannot get the nth 'element' in Fib
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # initialization
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b # calculate the next value
        if self.a > 100: # when to quit
            raise StopIteration() # quit the iteration
        return self.a
    
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

for i in Fib():
    print(i)

f = Fib()
print(f[5])
#%%
    
# __getitem__
# Used for getting the nth element in Fib
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1,1
        for x in range(n):
            a, b = b, a+b
        return a

f = Fib2()
print(f[1])
print(f[4])
#%%