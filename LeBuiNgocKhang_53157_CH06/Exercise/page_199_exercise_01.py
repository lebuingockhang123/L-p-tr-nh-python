"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write the code for a mapping that generates a list of the absolute values of the numbers in a list
named number

Solution:
[1, 2, 66, 79]

"""
numbers = [1, -2, -66, 79]
result = list(map(abs, numbers))
print(result)