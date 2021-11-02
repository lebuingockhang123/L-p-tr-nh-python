"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the
file.


Solution:

Hello
My name is Khang
print("Khang Le")


"""
file_object = open("myfile.txt",'r')
data = file_object.read()
print(data)