"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can
contain any of the printable ASCII characters. Suggest an algorithm for cracking this code.

Solution:

ifmmp"
jgnnq#
khoor$
lipps%

"""

def decoded(s):
    for i in range(1,5):
        string = ""
        for char in s:
            if(ord(char) + i > 126):
                charc = (ord(char) + i) - 4
                string =  string + chr(charc)
            else:
               charc = ord(char) + i
               string =  string + chr(charc)

        print(string)
decoded("hello!")

