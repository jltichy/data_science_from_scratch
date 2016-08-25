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
  """this is where you put an optional docstring that explains what the function does.  for example, this function multiplies its input by 2"""
  return x*2
  
x = 5
print double(x)
