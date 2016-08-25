#!/usr/bin/env python

for i in [1, 2, 3, 4, 5]:
  print i                   #first line in "for i" block
  for j in [1, 2, 3, 4, 5]:
    print j                 #first line in "for j" block
    print i+j               #last line in "for i" block
  print i                   #last line in "for i" block
print "done looping"

long_winded_computation = (1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+19+20)
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
easier_to_read_list_of_lists = [[1,2,3],
                                [4,5,6],
                                [7,8,9]]
                                
two_plus_three = 2 + \
                 3

import re
my_regex = re.compile("0-9+", re.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
My_counter = Counter()

match = 10
from re import *  #uh oh, re has a match function
print match       #"<function re.match>"

# from __future__ import division
# print '5 / 2' #This isn't working, and I'm not sure why.

def double(x):
  """this is where you put an optional : that explains what the 
  function does.  for example, this function multiplies its input by 2"""
  return x*2
  
x = 5
print double(x)

def apply_to_one(f):
  """calls the function f with 1 as its argument"""
  return f(1)

my_double = double    #refers to the previously defined function
x = apply_to_one(my_double) #equals 2
y = apply_to_one(lambda x: x + 4)   #equals 5
#another_double = lambda x: 2 * x    #don't do this
def another_double(x): return 2 * x #do this instead

def my_print(message="my default message"):
  print message

my_print("hello")     #prints 'hello'
my_print()            #prints 'my default message'

def subtract(a=0, b=0):
  return a - b
subtract(10,5) #returns 5
subtract(0,5)   #returns -5
subtract(b=5)   #also returns -5

