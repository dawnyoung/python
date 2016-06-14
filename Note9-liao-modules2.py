# -*- coding: utf-8 -*-

###############################################################################
#           hashlib
###############################################################################

# digest algorithm

# turn data with any length into a string with certain length (usually hexadecimal). 



# md5

# return 

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python '.encode('utf-8'))
md5.update('i do not know '.encode('utf-8')) # There should be a blank space after the 
                                             # sentence to make sure it is the same with 
                                             # the following whole sentence in one line.           
md5.update('let us check it out'.encode('utf-8'))
# if the data is long, we can use multiple update
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in python i do not know let us check it out'.encode('utf-8'))
print(md5.hexdigest())

# Writing the data in seperate lines or in the same line gets the same result.
#%%

# SHA 1
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python '.encode('utf-8'))
sha1.update('i do not know let us check it out'.encode('utf-8'))
print(sha1.hexdigest())
#%%

# Application: save password

def calc_md5(password):
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    print(pw_md5.hexdigest())

calc_md5('iampassword')
#%%

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    pw = hashlib.md5()
    pw.update(password.encode('utf-8'))
    pw = pw.hexdigest()
    if pw == db[user]:
        return True
    else:
        return False

print(login('michael', '123456'))
print(login('michael', '1234567'))
#%%

# salt
# use user name as salt

def get_md5(password):
    pw_md5 = hashlib.md5()
    pw_md5.update((password + 'the_Salt').encode('utf-8'))
    return pw_md5.hexdigest()

db = {}
def register(username, password):
    db[username] = get_md5(username + password + 'the-Salt')

register('michael', '123456')
#%%
    
def login(username, password):
    pw = get_md5(username + password + 'the-Salt')
    if pw == db[username]:
        return True
    else:
        return False
print(login('michael', '123456'))
print(login('michael', '1234567'))
#%%


###############################################################################
#         itertools
###############################################################################

import itertools

#   count

natuals = itertools.count(1) # endless iteration
for i in natuals:
    print(i)
# endless iteration
# ctrl + C to quit
#%%

# use takewhile to cut a limited sequence
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10, natuals) # stop when x > 10
print(list(ns))
#%%


#    cycle

abc = itertools.cycle('abc') # endless cycle
for a in abc:
    print(a)
# use ctrl + c to stop and quit
#%%

#    repeat

repeat = itertools.repeat('a', 3) # repeat a three times
for r in repeat:
    print(r)
#%%

#   chain
# link the iteration objects

for c in itertools.chain('abc','dd'):
    print(c)
#%%

#    groupby
# pick out the same characters which are next to each other, and put them together.
# different characters in different groups.
# the same characters but not next to each other in different groups.

for key, group in itertools.groupby('aadgllllddea'):
    print(key, list(group))
#%%
    
for key, group in itertools.groupby('AAaDDdGGgAAa', lambda c: c.upper()):
    print(key, list(group))
#%%