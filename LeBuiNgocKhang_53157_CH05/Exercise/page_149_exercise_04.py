"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Define a function named summation. This function expects two numbers, named low and high, as arguments.
The function computes and returns the sum of the numbers between low and high, inclusive.

Solution:


"""
low = int(input("Enter low: "))
high = int(input("Enter high: "))
def summation():
    sum = 0
    for i in (low, high):
        sum += i
    print(sum)
summation()