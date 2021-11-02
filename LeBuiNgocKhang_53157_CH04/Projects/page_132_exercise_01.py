"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using
a Caesar cipher. The script should work for any printable characters.

Solution:

Enter a message: hello world
Enter distance value: 3
khoor#zruog

"""

# Request the inputs
plainText = input("Enter a message: ")
distance = int(input("Enter distance value: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordvalue + 1)
    code += chr(cipherValue)
print(code)