"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Assume that the variables x and y refer to strings. Write a code segment that prints these strings in
alphabetical order. You should assume that they are not equal.


Solution:

The sorted words are:
bui
khang
le
ngoc

"""
# Program to sort alphabetically the words form a string provided by the user
my_str = "LE BUI NGOC KHANG"
# To take input from the user
#my_str = input("Enter a string: ")
# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)
