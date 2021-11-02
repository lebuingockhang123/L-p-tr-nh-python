"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a loop that replaces each number in a list named data with its absolute value.

Solution:
  Result the output:
The original list is : [2, -5, 7, -3, -9]
Absolute value list : [2, 5, 7, 3, 9]

"""
# initialize list
test_list = [2, -5, 7, -3, -9]
# printing original list
print("The original list is : " + str(test_list))
# using abs() + list comprehension
res = [abs(ele) for ele in test_list]
# printing result
print("Absolute value list : " + str(res))