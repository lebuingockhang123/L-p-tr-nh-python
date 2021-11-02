"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a script that decrypts a message coded by the method used in Project 6.

Solution:

Enter the coded text:0010011 1001101 1011011 1011011 1100001 011011 000011 0110001 1100001 1100111 1011011 1001011 000101
Hello, World!

"""

def bits2String(b=''):
    return chr(int(b,2) - 1)
#Implementation of shift method
def shift(n=''):
    temp = list(n)
    new = (temp[-1:] + temp[0:-1])
    ret = ''
    for i in new:
        ret += i
    return ret
#Get the input from user
coded = input('Enter the coded text:')
#split the code
process = coded.split()
decoded = ''
for q in process:
    decoded += bits2String(shift(q))
#Display the decoded message
print(decoded)

