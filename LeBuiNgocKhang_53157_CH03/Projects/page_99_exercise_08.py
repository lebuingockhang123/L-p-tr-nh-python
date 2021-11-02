"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly
divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers. You
can use this algorithm in the following manner:
a. Compute the remainder of dividing the larger number by the smaller
number.
b. Replace the larger number with the smaller number and the smaller number
with the remainder.
c. Repeat this process until the smaller number is zero
The larger number at this point is the GCD of A and B. Write a program that lets
the user enter two integers and then prints each step in the process of using the
Euclidean algorithm to find their GCD.

Solution:

Enter the smaller number: 8
Enter the larger number: 12
The greatest common divisor is:  8

"""
# request the input
first = int(input("Enter the smaller number: "))
second = int(input("Enter the larger number: "))

while first > 0:
    remender = first % second
    second = first
    first = remender

print("The greatest common divisor is: ",second)