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
    
    def __getitem__(self, n): # make it possible to get the nth element in Fib
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

for i in Fib():
    print(i)

f = Fib()
print(f[5])

# However, slice does not work on Fib
print(f[2:4]) # return an error
#%%
    
# __getitem__
# Used for getting the nth element in Fib
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1,1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
    

f = Fib2()
print(f[1])
print(f[4])
print(f[2:5])
#%%

# __setitem__ : give value
# __delitem__ : delete element

# __getattr__
class Student4(object):
    def __init__(self):
        self.name = 'kobe'
    def __getattr__(self, attr):
        if attr == 'score': # when there is no attribute called 'score'
            return 81 # return a number
        if attr == 'age':
            return lambda: 38 # return a function

s = Student4()
print(s.score)
print(s.age())
print(s.a) # return none by default

# If we did not define __getattr__, when calling an attr that does not exist, 
# an error will be returned.
#%%

class Student5(object):
    def __getattr__(self, attr):
        if attr == 'score':
            return 81
        raise AttributeError('\'Student5\' object has no attribute \'%s\'' % attr)
        # define error returned if the attr dose not exist

s = Student5()
print(s.score)
print(s.a)
#%%

callable(s) # s is an instance of Student5. it is not callable
s() # return an error
#%%

# __call__

class Student6(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('my name is %s' % self.name)

s2 = Student6('kobe')
print(callable(s2))
s2() # s2 is an instance of Student6. It is callable
#%%

###############################################################################
# Enum
###############################################################################

from enum import Enum

# give a constant value to each month
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', \
             'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '->', member, ',', member.value)
#%%

# give a constant value to each day
from enum import Enum, unique
@unique # make sure there is no replicated value
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Fri)
print(Weekday['Fri'])
print(Weekday.Fri.value)
print(Weekday(5))
for name, member in Weekday.__members__.items():
    print(name, '->', member, member.value)
#%%
    
###############################################################################
# type()
###############################################################################
    
print(type(s))
# type() returns the type of an object, or creates a new type.

def fn(self, name = 'world'): # define a function
    print('hello, %s' % name)

# create Hello class
Hello = type('Hello', (object,),  dict(hello = fn)) 
# type(name of class, base class, combine the class and the function)
# name of class
# parent class: a tuple
# combine the class and the function

h = Hello()
print(type(h))
#%%

###############################################################################
#   metaclass
###############################################################################

# define metaclass -> create class -> create instance

# object relational mapping

' Simple ORM using metaclass '

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
#%%