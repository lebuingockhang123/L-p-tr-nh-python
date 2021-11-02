"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Assume that the variable myString refers to a string, and the variable reversedString refers to an empty
string. Write a loop that adds the characters from myString to reversedString in reverse order

Solution:
o
ol
oll
olle
olleH

"""
if __name__ == '__main__':
    mystring = "Hello"
    reversedString = ""
    for i in mystring[::-1]:
        reversedString = reversedString + i
        print(reversedString)