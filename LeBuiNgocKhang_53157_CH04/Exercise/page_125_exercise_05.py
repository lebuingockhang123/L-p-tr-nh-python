"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:Write a code segment that prompts the user for a filename. If the file exists, the program should print
its contents on the terminal. Otherwise, it should print an error message


Solution:
Enter a file name: hello
Error: the file does not exist!

Enter a file name: myfile.txt
Hello
My name is Khang
print("Khang Le")


"""
from os.path import exists
fileName = input("Enter a file name: ")
if not exists(fileName):
    print("Error: the file does not exist!")
else:
    inputFile = open(fileName, 'r')
    print(inputFile.read())