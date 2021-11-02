"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a format operation that builds a string for the float variable amount that has exactly two digits
of precision and a field width of zero

Solution:

Your salary is $ 247.31

"""
# request the input float variable amount
amount = 247.310
# display the output
print ("Your salary is $ " +  ("%0.2f" %amount))