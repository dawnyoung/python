# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:35:04 2016

@author: Administrator
"""

#----------------------------------------------------------------------------------------------
#   Advanced Object Oriented Programming
#----------------------------------------------------------------------------------------------

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000

nums = []
while True:
  n = input("Enter a number: ")
  if n == "done":
      print('Invalid input')
      break
  try:
      nums.append(int(n))
  except ValueError:
      print ("Invalid input")

print ("Min: %d" % min(nums))
print ("Max: %d" % max(nums))