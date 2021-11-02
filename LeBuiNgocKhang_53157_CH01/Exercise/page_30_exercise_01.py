"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Suppose your script attempts to print the value of a variable that has not yet been assigned a value.
How does the Python interpreter react?
Solution:
    If any variable is not assigned any value then trying to print that variable will results into an error message
as "variable_name not defined".
    The interpreter checks for syntax errors. It will check the value of variable before printing it and if not
found then it returns the error.

    ....
"""