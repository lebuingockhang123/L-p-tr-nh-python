"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Using the value of data from Exercise 1, write the values of the following
expressions:
a. data.endswith('i')
b. " totally ".join(data.split())

Solution:

a. False
b. Python totally rules!

"""
# string data page 118 exercise 01
data = "Python rules!"

# data.endswith('i')
s = data.endswith('i')
print(s)

# " totally ".join(data.split())
string_one = " totally "
string_two = data.split()
print(string_one.join(string_two))