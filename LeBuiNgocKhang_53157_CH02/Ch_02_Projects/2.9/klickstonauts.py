"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that takes as input a number of kilometers and prints the corresponding number of nautical
miles. Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North
Pole and the equator.
• A nautical mile is 1 minute of an arc

Solution:

Enter the number of kilometer: 2360.44
The number of nautical miles is:  1274.6376


"""
# request the input
kilometers= float(input("Enter the number of kilometer: "))
# compute the results
nauticalmile = 90 * 60 * kilometers / 10000.0
# display the results
print("The number of nautical miles is: ",nauticalmile)