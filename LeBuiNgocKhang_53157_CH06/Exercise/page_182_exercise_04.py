"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Explain what happens when the following recursive function is called with the value 4 as an argument:
def example(n):
   if n > 0:
        print(n)
        example(n - 1)

Solution:
- First, function will check condition. With value = 4 > 0, function will run and print 4.
- Second, function example is called, that is recursion. Currently, n = 3 and print 3
- Continue,.... n = 2 and n = 1 will printed.
- When, n = 0, don't satisfy condition, program will stop.

"""