"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted in a
column that is right-justified, with a field width of 12 and a precision of 2.

Solution:
        3.24
       43.32
      123.53
      129.08
       14.46
        1.79
      201.45
      358.23
       52.15


"""
# list the input salaries
salaries = [3.241, 43.32, 123.53, 129.079, 14.463, 1.789, 201.45, 358.23, 52.145]
# iterating the loop
for i in salaries:
# display the width of 12 and a precision of 2
    print("%12.2f" %i)

