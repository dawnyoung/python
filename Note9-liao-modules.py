# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------------------
#                           modules
#---------------------------------------------------------------------------------------------

###############################################################################
#           datetime
###############################################################################

# get the current time (local time)

import datetime
print(datetime.datetime.now()) # the first datetime is the module
                               # the second datetime is the class inside the module
#%%

from datetime import datetime
print(datetime.now()) # the datetime is the class
#%%

dt = datetime(2016, 6, 9, 10, 21) # 6/9/2016, 10:21
print(dt)
#%%

#  datetime  ->  timestamp

# epoch time: 1970-1-1, 00:00:00, UTC+00:00
# timestamp: how many seconds after the epoch time. 
#            after is positive. before is negative.

# timestamp is a float. the decmal indicates the millisecond

from datetime import datetime
dt = datetime(2016, 6, 9, 10, 21)
dt.timestamp()
#%%

#  datestamp  ->  datetime
from datetime import datetime
t = 100000000
print(datetime.fromtimestamp(t)) # local time
print(datetime.utcfromtimestamp(t)) # UTC
#%%

#  str  ->  datetime

from datetime import datetime
cday = datetime.strptime('2016-06-09 10:50:00', '%Y-%m-%d %H:%M:%S')
print(cday)
#%%

#  datetime  ->  str
from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M')) # weekday, month, date, hour: minute
#%%

#  calculate time

from datetime import datetime, timedelta
now = datetime.now()
print(now + timedelta(days = 2, hours = 18))
#%%

#  local time  ->  UTC, other time zone

from datetime import datetime, timedelta, timezone

# utc time
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)

# local time (illinois)
il_dt = utc_dt.astimezone(timezone(timedelta(hours = -5)))
print(il_dt)
# get local directly to compare with the local got from utc time
print(datetime.now())

# get Beijing time from local time
bj_dt = il_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
#%%

# date and time format

#--------------------------------------------------------------------
#  Directive   |  Meaning
#--------------------------------------------------------------------
#      %a      | weekday as locale's abbreviated name
#      %A      | weekday as locale's full name
#      %w      | weekday as a decimal number, where 0 is Sun and 6 is Sat
#      %d      | day of the month as a zero-padded decimal number
#      %b      | month as locale's abbreviated name
#      %B      | month as locale's full name
#      %m      | month as a zero-padded decimal number
#      %y      | year without century as a zero-padded decimal number
#      %Y      | year with century as a decimal number
#      %H      | hour(24 hour clock) as a zero-padded decimal number
#      %I      | hour(12 hour clock) as a zero-padded decimal number
#      %p      | locale's equivalent of either AM or PM
#      %M      | minute as a zero-padded decimal number
#      %S      | second as a zero-padded decimal number
#      %f      | microsecond as decimal number, zero-padded on the left
#      %z      | utc offset in the form +HHMM or -HHMM (empty string if the object is naive)
#      %Z      | time zone name (empty string if the object is naive)
#      %j      | day of the year as a zero-padded decimal number
#      %U      | week number of the year (Sunday as the first day of the week)
#                as a zero-padded decimal new year preceding the first Sunday are
#                considered to be in week 0
#      %W      | week number of the year (Monday as the first day of the week)
#                as a decimal number. All days in a new year preceding the first 
#                considered to be in week 0.
#      %c      | locale's appropriate date and time representation
#      %x      | locale's appropriate date representation
#      %X      | locale's appropriate time representation
#      %%      | a literal '%' character
#--------------------------------------------------------------------

###############################################################################
#             collections
###############################################################################

#  namedtuple
from collections import namedtuple

# make a tuple a coordinates
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)
#%%

# make a tuple a circle
Circle = namedtuple('Circle', ['x', 'y', 'r']) # the centre of a circle and the radius
#%%

#  deque
# used for list and stack. 
# to delete and insert quickly

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
print(q)
q.appendleft('y')
print(q)
isinstance(q, list) # q is not a list
#%%

#  defaultdict
# when key dose not exist, return a default value

from collections import defaultdict
dd = defaultdict(lambda: 'N/A') # set the default value
dd['k1'] = 'key1'
print(dd['k1']) # this key exists
print(dd['k2']) # this key does not exist, return the dafualt value: N/A
#%%

#  OrderedDict
# when using dict, keys are unordered
# use OrderedDict to keep it in order

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

# ordered by the input order
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
#%%

#fifo: first in, first out
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
#%%
        
#  counter
        
# counter is a subclass of dict

from collections import Counter
c = Counter()
for ch in 'abcdddfegrtndiognoag':
    c[ch] = c[ch] + 1

print(c)
#%%

###############################################################################
#                base64
###############################################################################

# show any binary data with 64 characters

# 64 characters: A,B,...,Z,a,b,...,z,0,1,...,9,+,/

import base64

print(base64.b64encode(b'binarycode12345'))

print(base64.b64decode(b'YmluYXJ5Y29kZTEyMzQ1'))
#%%

###############################################################################
#          struct
###############################################################################

# turn any data into bytes.

import struct
struct.pack('>I', 109264738)
# > : big-endian
# I : 4 bytes, int with not character
#%%

import struct
def bmpinfo(s):
    try:
        s = struct.unpack('<ccIIIIIIHH', s)
        if s[0]==b'B' and s[1]==b'M':
            print('This is a windows bitmap')
        elif s[0]==b'B' and s[1]==b'A':
            print('this is an OS/2 bitmap')
        else:
            print('this is not a bitmap')
    finally:
        print('finally...')
s = open('d:\Math HW10.jmp', 'rb').read(30)
bmpinfo(s)
#%%