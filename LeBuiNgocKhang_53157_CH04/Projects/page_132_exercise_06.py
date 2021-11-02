"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5
to code a new encryption algorithm. The algorithm should add 1 to each character’s numeric ASCII value, convert
it to a bit string, and shift the bits of this string one place to the left. A single-space character in the
encrypted string separates the resulting bit strings.

Solution:

Enter a message: Hello, World!
0010011 1001101 1011011 1011011 1100001 011011 000011 0110001 1100001 1100111 1011011 1001011 000101

"""
plainText = input("Enter a message: ")

code = ""
for ch in plainText:
    ordValue = ord(ch) + 1
    bstring = ""
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        bstring = str(remainder) + bstring
    # shift one bit to left
    if len(bstring) > 1:
        bstring = bstring[1:] + bstring[0]
    # Add encrypted character to code string
    code += bstring + " "
print(code)