"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a
Caesar cipher. The script should work for any printable characters

Solution:

Enter the coded text: khoor#zruog
Enter the distance value: 3
hello world

"""
# Request the inputs

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < 0:
        cipherValue = 127 - (distance - (1- ordvalue))
    plainText += chr(cipherValue)
print(plainText)