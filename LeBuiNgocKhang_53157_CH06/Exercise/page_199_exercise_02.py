"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function.

Solution:
[1, 79]

"""
numbers = [1, -2, -66, 79]
result = list(filter(lambda x: x > 0, numbers))
print(result)