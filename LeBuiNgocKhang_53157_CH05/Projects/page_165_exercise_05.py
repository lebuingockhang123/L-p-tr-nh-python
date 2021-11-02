"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: In Chapter 4, we developed an algorithm for converting from binary to decimal. You can generalize this
algorithm to work for a representation in any base.
Instead of using a power of 2, this time you use a power of the base. Also, you use
digits greater than 9, such as A . . . F, when they occur. Define a function named
repToDecimal that expects two arguments, a string, and an integer. The second
argument should be the base. For example, repToDecimal("10", 8) returns
8, whereas repToDecimal("10", 16) returns 16. The function should use a
lookup table to find the value of any digit. Make sure that this table (it is actually
a dictionary) is initialized before the function is defined. For its keys, use the 10
decimal digits (all strings) and the letters A . . . F (all uppercase). The value stored
with each key should be the integer that the digit represents. (The letter 'A' associates with the integer value
10, and so on.) The main loop of the function should convert each digit to uppercase, look up its value in the
table, and use this value in the computation. Include a main function that tests the conversion function
with numbers in several bases.

Solution:

1
1
1
1

"""

def repToDecimal(str, base):
    result = 0
    # initializing a dictionary
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
    for i in str:
        n = dict[i]
        result = base * result + n
        return result


# calling the method and displaying the result
print(repToDecimal('10', 10))
print(repToDecimal('10', 8))
print(repToDecimal('10', 2))
print(repToDecimal('10', 16))