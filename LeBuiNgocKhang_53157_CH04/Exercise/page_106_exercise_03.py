"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Assume that the variable myString refers to a string. Write a code segment that uses a loop to print the
characters of the string in reverse order.

Solution:
H
e
l
l
o

"""

if __name__ == '__main__':
    mystring = "Hello"
    for i in range(len(mystring)):
        print(mystring[i])