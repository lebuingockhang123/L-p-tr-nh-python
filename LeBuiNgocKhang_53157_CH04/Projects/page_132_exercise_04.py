"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Octal numbers have a base of eight and the digits 0–7. Write the scripts octalTo-Decimal.py and
decimalToOctal.py, which convert numbers between the octaland decimal representations of integers. These scripts
use algorithms that aresimilar to those of the binaryToDecimal and decimalToBinary scripts developed in Section
4-3.

Solution:

# File: binarytodecimal
Enter a string of bits: 3444
The integer value is 52
# File: decimaltobinary
Enter a decimal integer: 12
Quotient Remainder Binary
    6       0           0
    3       0          00
    1       1         100
    0       1        1100
The binary representation is 1100


"""


# Converts a string of bits to a decimal integer.
bstring = input("Enter a string of bits: ")
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)

# Converts a decimal integer to a string of bits
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bstring = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (decimal, remainder, bstring))
    print("The binary representation is", bstring)