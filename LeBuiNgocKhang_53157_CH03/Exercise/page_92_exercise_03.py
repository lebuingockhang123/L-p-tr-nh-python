"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  The log 2 of a given number N is given by M in the equation N 5 M2 . Using integer arithmetic, the value
of M is approximately equal to the number of times N can be evenly divided by 2 until it becomes 0. Write a loop
that computes this approximation of the log 2 of a given number N. You can check your code by importing the
math.log function and evaluating the expression round(math.log(N, 2)) (note that the math.log function returns a
floating-point value).


Solution:

Enter N: 15
15.0
7.0
3.0
1.0
Approx log 15.0

"""
import math
n = float(input("Enter N: "))
m = 0
original = n
while n != 0:
    print(n)
    m += 1
    n //= 2
print("Approx log " + str(round(math.log(original),2)))