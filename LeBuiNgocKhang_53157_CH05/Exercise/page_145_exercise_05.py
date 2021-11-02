"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Assume that data refers to a list of numbers, and result refers to an empty list. Write a loop that
adds the nonzero values in data to the result list, keeping them in their relative positions and excluding the
zeros.

Solution:
  Result the output:
  [[3, 7, 2, 9], [3, 7, 2, 9], [3, 7, 2, 9], [3, 7, 2, 9]]

"""
list = [3, -7, 2, -9]
result = []
index = 0
while index<len(list):
    list[index] = abs(list[index])
    index += 1
    result.append(list)
print(result)