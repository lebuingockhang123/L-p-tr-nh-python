"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  The factorial of an integer N is the product of the integers between 1 and N, inclusive. Write a while
loop that computes the factorial of a given integer


Solution:

Enter a number: 4
Factorial is:  24

Enter a number: 5
Factorial is:  120

"""
# Request the number
num = int(input("Enter a number: "))
fact = 1
while num > 1:
    fact = fact * num
    num -= 1
# display the Factorial
print("Factorial is: ", fact)

