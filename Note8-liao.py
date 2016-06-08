# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------
#                regular expression
#-----------------------------------------------------------------------------------------------------

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

###############################################################################
#    basic
###############################################################################

# \d       ->     a digit (00\d   ->   007, or 008, or 003 .....)

# \w       ->     a digit or a letter (00\w   ->  00d or 009)

#  .       ->     (one) anything (letter, digit, & $ $ % ^)

#   *      ->     zero or more

#   +      ->     at least one

#    ?     ->     zero or one

#  {n}     ->     n 

# {n, m}   ->     n to m

# Example:
#       \d{3}\s+\d{3,8}
# \d{3}    ->    3 digits
# \s+      ->    at least one blank space, such as ' ', '   '
# \d{3, 8} ->    3-8 digits
# Therefore, this can be:  123   34567

###############################################################################
#    advanced
###############################################################################

#  [0-9a-zA-Z\_]       ->    a digit, a letter (both lower and upper case or _)

#  [0-9a-zA-Z\_]+      ->    at least one above things

# [a-zA-Z\_][0-9a-zA-Z\_]*    ->    one or more characters
#                                   the first is [a-zA-Z\_]: lower/upper case letter or a _
#                                   the second is [0-9a-zA-Z\_]*: zero or more

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}   ->    same with the above
#                                        except that the length of the second one 
#                                        should be 0 - 19.

# a|b     ->     a or b

#   ^     ->     beginning. ^\d: must starts with a digit

#   $     ->     end.    \d$: must end with a digit
#%%



###############################################################################
#                    re module
###############################################################################

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
#%%

# split a string
print('a b    c'.split(' '))
# return: ['a', 'b', '', '', '', 'c']

print(re.split(r'[\s\,]+', 'a b    c'))
# return: ['a', 'b', 'c']
#%%

# group
# group can be shown by ()
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

print(m.group(0)) # the whole string. the original
print(m.group(1)) # the first group
print(m.group(2)) # the second group
#%%

###############################################################################
#              greedy match
###############################################################################

# match as much characters as possible.

# add ? to make it not greedy match (match as few characters as possible)

print(re.match(r'^(\d+)(0*)$', '102300').groups())
# (\d+) is greedy match. so this part matches with the 00 at the end of this string.
# Therefore, (0*) can noly match a empty string

print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# (\d+?) is not greedy match. 
#%%

###############################################################################
#                   compile
###############################################################################

import re

# compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# use it
re_telephone.match('010-8820').groups()
#%%

import re

re_email = re.compile(r'([0-9a-zA-Z\_]+)(@[a-z]+.com$)')

email = re_email.match('someone@gmail.com').groups()

print('<', email[0], '>', '  ', re_email.match('someone@gmail.com').group(0))