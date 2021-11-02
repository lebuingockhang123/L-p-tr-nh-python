"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Assume that the variable data refers to the string "Python rules!". Use a string method from Table 4-2
to perform the following tasks:
a. Obtain a list of the words in the string.
b. Convert the string to uppercase.
c. Locate the position of the string "rules".
d. Replace the exclamation point with a question mark.

Solution:
Python rules!
PYTHON RULES!
7
Python rules?

"""
# string
data = "Python rules!"

# Obtain a list of the words in the string
print(data.strip())
# Convert the string to uppercase.
print(data.upper())
# Locate the position of the string "rules".
print(data.find('rules'))
# Replace the exclamation point with a question mark.
print(data.replace('!', '?'))