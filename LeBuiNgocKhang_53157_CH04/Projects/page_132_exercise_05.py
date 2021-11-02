"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: A bit shift is a procedure whereby the bits in a bit string are moved to the left or to the right. For
example, we can shift the bits in the string 1011 two places to the left to produce the string 1110. Note that
the leftmost two bits are wrapped around to the right side of the string in this operation. Define two scripts,
shiftLeft.py and shiftRight.py, that expect a bit string as an input. The script shiftLeft shifts the bits in its
input one place to the left, wrapping the leftmost bit to the rightmost position. The script shiftRight performs
the inverse operation. Each script prints the resulting string.

Solution:
+ shiftLeft
Enter a string of bits: 10111
01111
+ shiftRight
Enter a string of bits: 4906
6490

"""

# shiftLeft
bits = input("Enter a string of bits: ")
if len(bits) > 1:
    bits = bits[1:] + bits[0]
print(bits)

# shiftRight
bits = input("Enter a string of bits: ")
if len(bits) > 1:
    bits = bits[len(bits) - 1] + bits[0: len(bits) - 1]
print(bits)

