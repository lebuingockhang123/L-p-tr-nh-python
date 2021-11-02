"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Assume that the variable teststring refers to a string. Write a loop that prints each character in this
string, followed by its ASCII value.

Solution:

Please Enter your Own String : student
The ASCII Value of Character s = 115
The ASCII Value of Character t = 116
The ASCII Value of Character u = 117
The ASCII Value of Character d = 100
The ASCII Value of Character e = 101
The ASCII Value of Character n = 110
The ASCII Value of Character t = 116


"""
# Python program to find ASCII Values of Total Characters in a String

str1 = input("Please Enter your Own String : ")
i = 0

while (i < len(str1)):
    print("The ASCII Value of Character %c = %d" % (str1[i], ord(str1[i])))
    i = i + 1
