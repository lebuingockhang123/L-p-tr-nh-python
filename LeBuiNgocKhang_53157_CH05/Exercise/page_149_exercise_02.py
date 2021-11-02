"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Define a function named even. This function expects a number as an argument and
returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A
number is evenly divisible by 2 if the remainder is 0.)

Solution:
16 is even
33 is odd
2 is even
15 is odd
99 is odd
100 is even
1 is odd
18 is even

"""
numbers = [16,33,2,15,99,100,1,18]
def is_even(number):
    if number % 2 == 0:
        print (number,"is even")
        return True
    else:
        print (number, "is odd")
        return False
for number in numbers:
    is_even(number)