"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Assume that x refers to a number. Write a code segment that prints the number’s absolute value with outu
sing Python’s abs function

Solution:

Enter a number: -3
3
Enter a number: 5
-5

"""
x = int(input("Enter a number: "))
if x > 0 or x < 0:
    x = -x
    print(x)

