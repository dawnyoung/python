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