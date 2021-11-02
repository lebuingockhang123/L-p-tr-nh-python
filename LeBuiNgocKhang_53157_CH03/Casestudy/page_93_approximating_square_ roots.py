"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that computes square roots.


Solution:
STEP 1: Analysis
    The input to this program is a positive floating-point number or an integer. The output is a floating-point number representing the square root of the input number. For
purposes of comparison, we also output Python’s estimate of the square root using
math.sqrt.
STEP 2: Design
    In the seventeenth century, Sir Isaac Newton discovered an algorithm for approximating the square root of a
positive number. Recall that the square root y of a positive number x is the number y such that y x 2 5 . Newton
discovered that if one’s initial estimate of y is z, then a better estimate of y can be obtained by taking the
average of z together with x / z. The estimate can be transformed by this rule again and again, until a
satisfactory estimate is reached.
STEP 3: Implementation (Coding)
    The code for this program is straightforward.
Program: newton.py
Author: Ken
Compute the square root of a number.
1. The input is a number.
2. The outputs are the program's estimate of the square root
using Newton's method of successive approximations, and
Python's own estimate using math.sqrt.
STEP 4: Testing
    The valid inputs to this program are positive integers and floating-point numbers. The display of Python’s
own most accurate estimate of the square root provides a benchmark for assessing the correctness of our own
algorithm.

- RESULT THE OUTPUT:
Enter a positive number: 35
The program's estimate: 5.916079786951165
Python's estimate:  5.916079783099616

"""
import math
# Receive the input number from the user
x = float(input("Enter a positive number: "))
# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0
# Perform the successive approximations
while True:
 estimate = (estimate + x / estimate) / 2
 difference = abs(x - estimate ** 2)
 if difference <= tolerance:
    break
# Output the result
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(x))