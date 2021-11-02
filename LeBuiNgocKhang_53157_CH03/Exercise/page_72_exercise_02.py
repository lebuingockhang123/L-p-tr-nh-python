"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a code segment that displays the values of the integers x, y, and z on a single line, such that
each value is right-justified with a field width of 6.

Solution:

Enter first number: 4
Enter second number: 7
Enter third number: 2
     4      7      2

"""
# request the input
x = int(input ("Enter first number: "))
y = int(input ("Enter second number: "))
z = int(input ("Enter third number: "))
# display the value
print('%6d %6d %6d' %(x,y,z))