"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Light travels at 3*10**8 Light travels per second. A light-year is the distance a light beam travels in one year.
Write a program that calculates and displays the value of a light-year.

Solution:

Light travels 9460800000000000 meter in a years.

"""
# request the input
lightSpeed= 3 * 10 ** 8
# compute the results
seconds= 365 * 24 * 60 * 60
light_year= lightSpeed * seconds
# display the results
print("Light travels",light_year,"meter in a years. ")