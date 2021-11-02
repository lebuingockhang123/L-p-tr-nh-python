"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Explain what happens when the following recursive function is called with the value 4 as an argument:
def example(n):
    if n > 0:
        print(n)
        example(n)
    else:
        example(n - 1)

Solution:
- With n = 4 > 0, this function will be called many times and print many value = 4

"""