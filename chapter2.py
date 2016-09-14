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
print first_three         #[-1,1,2]
three_to_end = x[3:]
print three_to_end        #[3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5]
print one_to_four         #[1, 2, 3, 4]
last_three = x[-3:]
print last_three          #[7, 8, 9]
without_first_and_last = x[1:-1]
print without_first_and_last    #[1, 2, 3, 4, 5, 6, 7, 8]
copy_of_x = x[:]
print copy_of_x                 #[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]


a = 1 in [1,2,3]
print a           #true
b = 0 in [1,2,3]
print b           #false

#Concatenate lists:
x = [1,2,3]
x.extend([4, 5, 6])
print x             #x is now [1, 2, 3, 4, 5, 6]

# or

x = [1, 2, 3]
print x
y = x+[4, 5, 6]
print y

x =[1, 2, 3]

x.append(0)
print x           #x is now [1, 2, 3, 0]

y = x[-1] 
print y           #equals 0
z = len(x)
print z           #equals 4

#unpack lists:
x,y = [1,2]
print x           #x is now 1
print y           #y is now 2

#if we don't care about the first element, we can do this:
_,y = [1,2]       #now y is equal to 2 but it doesn't matter what the first element is

#Tuples - page 21
my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3 #my_list is now [1,3]

try:
  my_tuple[1] = 3
except TypeError:
  print "cannot modify a tuple"

def sum_and_product(x,y):
  return (x+y),(x*y)
sp = sum_and_product(2,3) #equals (5,6)
print sp
s,p = sum_and_product(5,10) #s is 15, p is 50
print s
print p

#Tuples and lists can also be used for multiple assignments:
x,y = 1,2   #now x is 1 and y is 2
x,y = y,x   #Pythonic way to swap variables; now x is 2 and y is 1

#Dictionaries - page 21
empty_dict = {}       #Pythonic
empty_dict2 = dict()  #less Pythonic
grades = {"Joel":80, "Tim":95}  #dictionary literal
joels_grade = grades["Joel"]

try:
  kates_grade = grades["Kate"]
except KeyError:
  print "no grade for Kate"
  
joel_has_grade = "Joel" in grades #True
kate_has_grade = "Kate" in grades #False

joels_grade = grades.get("Joel", 0)   #equals 80
kates_grade = grades.get("Kate", 0)   #equals 0
no_ones_grade = grades.get("No One")  #default - default is none

#note that there is a break here in the code for chapter 2.  it was 
#getting to be too tedious and not necessary.

#control flow - page 25

if 1>2:
  message = "if only 1 were greater than two..."
elif 1>3:
  message = "elif stands for 'else if'"
else:
  message = "when all else fails use else (if you want to)"
  
parity = "even" if x%2==0 else "odd"

#we can also use while loops
x = 0
while x<10:
  print x, "is less than 10"
  x += 1
#although more often we should use for and in, like this:
for x in range(10):
  print x, "is less than 10"
  
#or something like this:
for x in range(10):
  if x==3:
    continue    #go immediately to the next iteration
  if x==5:
    break       #quit the loop entirely
print x
#this will print 0,1,2, and 4

#start with truthiness - page 25
one_is_less_than_two = 1<2  #equals true
true_equals_false = True == False   #equals false
x = None
print x == None     #prints True, but is not Pythonic
print x is None     #prints True, and is Pythonic


def some_function_that_returns_a_string():
  return 'astring'

#I'm not sure what this does:
s = some_function_that_returns_a_string()
if s:
  first_char = s[0]
else:
  first_char = ""

#The book tells us we can do this instead:
first_char = s and s[0]

#and then it goes on to describe this:
safe_x = x or 0
print safe_x
#the book says that this is definitely a number

#sorting - page 27
x = [4,1,2,3]
y = sorted(x)   #is [1,2,3,4], x has not changed
x.sort()        #now x is [1,2,3,4]

#we can also sort by absolute value -- the above ex. uses the default of s to b
x = sorted([-4,1,-2,3], key=abs, reverse=True)    #is[-4,3,-2,1]

# #sort the words and counts from highest count to lowest
# wc = sorted(word_counts.items(),
#             key=lambda (word,count): count,
#             reverse = True)
            
#there is an error in the above code, but I don't know what it is.  

#list comprehensions - for transforming lists into other lists
even_numbers = [x for x in range(5) if x % 2 == 0]      #[0,2,4]
squares = [x * x for x in range(5)]                     #[0,1,4,9,16]
even_squares = [x * x for x in even_numbers]            #[0,4,16]
print even_squares

square_dict = { x : x * x for x in range(5) }           #{ 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set = { x * x for x in [1, -1] }                 #{ 1 }
zeroes = [0 for _ in even_numbers]          #has the same length as even_numbers
pairs = [(x,y)
          for x in range(10)
          for y in range(10)]           #100 pairs (0,0) (o,1) ... (9,8), (9,9)
print pairs
  

increasing_pairs = [(x,y)                     #only pairs with x<y
                    for x in range(10)        #range(lo,hi) equals
                    for y in range(x+1, 10)]  #[lo, lo + 1, ..., hi -1]
print increasing_pairs

#Generators and Iterators - page 28
def do_something_with(i):
  print("i")
  
def lazy_range(n):
  """a lazy version of range"""
  i = 0
  while i < n:
    yield i
    i +=1
for i in lazy_range(10):
  do_something_with(i)
  
def natural_numbers():
  """returns 1,2,3,..."""
  n=1
  while True:
    yield n
    n += 1

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
for ele in lazy_evens_below_20:
  print(ele)
print lazy_evens_below_20

#the above topic is still a little foggy - i need to work on this more

#randomness - page 29
import random
four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms
#random.random() produces numbers uniformly between 0 and 1.  it's the random
#function we'll use most often

#the random seed function gives reproducible results:
random.seed(10)       #set the seed to 10
print random.random() #will give some random number 
random.seed(10)       #set the seed to 10 again
print random.random() #gives the same "random" number as before

