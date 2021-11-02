"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write the code for a reducing that creates a single string from a list of strings named words.

Solution:
hello

"""

from functools import reduce

def add(x, y):
    return x + y

words = ["h", "e", "l", "l", "o"]
result = reduce(add, words)
print(result)