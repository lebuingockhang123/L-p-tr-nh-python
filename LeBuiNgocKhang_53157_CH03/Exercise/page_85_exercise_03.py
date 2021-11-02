"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Write a loop that counts the number of space characters in a string. Recall that the space character
is represented as ' '.


Solution:

Number of spaces:  2

"""


def check_space(string):
    count = 0
# loop for search each index
    for i in range(0, len(string)):
# Check each char
         if string[i] == " ":
            count += 1
    return count
# string assignment
string = "hello world 123"
# display string
print("Number of spaces: ", check_space(string))