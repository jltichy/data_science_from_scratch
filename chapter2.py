#!/usr/bin/env python

from __future__ import division

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

#from __future__ import division  #Note that this is now at the beginning of the file.
print 5/2 #This isn't working, and I'm not sure why.

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

single_quoted_string = 'data science'
print single_quoted_string
double_quoted_string = "data science"
print double_quoted_string

tab_string = "\t"   #represents the tab character
len(tab_string)     #is 1
not_tab_string = r"\t"    #represents the characters '\' and 't'
len(not_tab_string) #is 2

multi_line_string = """This is the first line
and this is the second line
and this is the thrid line"""

try:
    print 0/0
except ZeroDivisionError:
    print "cannot divide by zero"

#print 10/0

integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
print heterogeneous_list
list_of_lists = [integer_list, heterogeneous_list, []]
print list_of_lists
list_length = len(integer_list)   #equals 3
list_sum = sum(integer_list)           #equals 6
print list_sum

x = range(10)             #is the list [0,1,...,9]
print x
zero = x[0]               #equals 0, lists are 0-indexed
one = x[1]
nine = x[-1]              #equals 9, 'Pythonic' for last element
eight = x[-2]             #equals 8, 'Pythonic' for next to last element
x[0] = -1                 #now x is [-1,1,2,3,...,9]
first_three = x[:3]       #[-1,1,2]
print first_three

