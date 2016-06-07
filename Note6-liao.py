# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------
#           IO (Input/Output)
#------------------------------------------------------------------------------------------

# synchronous IO 
# asynchronous IO

###############################################################################
#     read/write files
###############################################################################

f = open('file.py', 'r') # read only

f.read() # read the file into internal storage

f.close() # close the file to save memory

# f is a file-like object
#%%

# If there are errors when open or read, the close() will not be excuted. 
# We can use this code to make sure the file can be closed 

try:
    f = open('file.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#%%
        
# Another way to do this
with open('file.py', 'r') as f:
    print(f.read())
#%%
    
# read large file
f.read(4) # read 4 kb 

# read line by line
for line in f.readlines():
    print(line.strip()) # strip: delete the \n at the end
#%%

# binary file
f = open('file.jpg', 'rb') # read binary file
f.read()
#%%

# character encoding
# non UTF-8 coded file

f = open('file.txt', 'r', encoding = 'gbk', errors = 'ignore') # ignore the illegal character
#%%

f = open('text.txt', 'w')
f.write('hello world')
f.close() # necessary to save the content we write
#%%

# another way to write
with open('file2.txt', 'w') as f:
    f.write('hello world \nhello you') #\n: change to the next line
#%%

###############################################################################
#    StringIO and BytesIO
###############################################################################

# does not read or write a file, but in internal memory

# StringIO: str
from io import StringIO
f = StringIO() # create a stringIO
f.write('hello') # write
f.write(' ')
f.write('world')
print(f.getvalue()) # print f
#%%

# stringIO can be read like a file
from io import StringIO
f = StringIO('hello\nworld\nhow are you')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# no need to close
    
# f.readline() or f.write(). These two function cannot be used together.
#%%
    
# BytesIO: binary data
from io import BytesIO
f = BytesIO()
f.write('代码'.encode('utf-8')) # write utf-8 encoded bytes, not string
print(f.getvalue())
#%%

from io import BytesIO
f = BytesIO(b'\xe4\xbb\xa3\xe7\xa0\x81')
f.read()
#%%

###############################################################################
#   files and path
###############################################################################

# enviroment variables
import os # operating system
print(os.name) # what os? Linux, Mac, Windows?
               # nt means windows.posix means others.
# os.uname() gives more details about os, but it dose not work on Windows.
# os function is related to what os is used.

print(os.environ) # show all enviroment variables
os.environ.get('SESSIONNAME') # get a value for the enviroment variable by key
                              # SESSIONNAME is the key
#%%

# path

os.path.abspath('.') # the absolute path

# create a new directory
os.path.join('D:\\python', 'newdir')  # show the path of the new dir
os.mkdir('D:\\python\\newdir') # create

os.rmdir('D:\\python\\newdir') # remove a dir
#%%

# files
os.path.split('D://python/python/test.txt')
os.path.splitext('D://python/python/test.txt')

os.rename('text.txt', 'file.txt') # rename the text.txt to file.txt

os.remove('file.txt') # delete this file
#%%

# list all the dir in the current dir
[x for x in os.listdir('.') if os.path.isdir(x)]

# list all the py files in the current dir
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
#%%

# find all the files that have 'liao' in their names in the current dir and all the dirs
# in the current dir
def FindFile(filename, value):
    try:
        dirlist = os.listdir(filename)
        for x in dirlist:
            tmp = os.path.join(filename,x)
            if os.path.isdir(tmp):      #tmp must be absolute path
                FindFile(tmp, value)
            elif os.path.isfile(tmp):  
                if value in x:      
                    print(tmp)
    except Exception as e:
        print(e)

FindFile('.', 'liao')
#%%

###############################################################################
#                 pickling
###############################################################################

# pickle the variable to make it savable

import pickle
d = dict(name = 'bob', age = 20, score = 80)
pickle.dumps(d) # turn d into bytes

f = open('dump.txt', 'wb') # write binary variables
pickle.dump(d, f) # turn d into a file-like object and save it in f
f.close()
#%%

f = open('dump.txt', 'rb') # read binary
d = pickle.load(f) # unpickling
f.close()
d

# Pickling can only be used for Python. 
# It is not compatible among different Python versions.
#%%

#  JSON can be used for different programming language.

#----------------------------------------
#   JSON type      |      Python type
#----------------------------------------
#     {}           |         dict
#     []           |         list
#    "string"      |         str
#    1234.56       |        int or float
#    ture/false    |        Ture/False
#     null         |        None
#----------------------------------------
#%%

# turn a Python object into json
import json
d = dict(name = 'bob', age = 20, score = 80)
json.dumps(d)
#%%

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
#%%

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
def Student2dict(std):
    return{
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

s = Student('bob', 39, 80)

json.dumps(s, default = Student2dict)
#%%

# json to python
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])

json.loads(json_str, object_hook = dict2Student)
#%%