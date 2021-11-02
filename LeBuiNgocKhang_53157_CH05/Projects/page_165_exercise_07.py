"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Write a program that inputs a text file. The program should print the unique words in the file in
alphabetical order.

Solution:

Enter the input File Name: inName
hello
world

"""
inName = input("Enter the input File Name: ")
inputFile = open(inName, 'r')
uniqueWords = []

for line in inputFile:
    words = line.split()
    for word in words:
        if not word in uniqueWords:
            uniqueWords.append(word)

uniqueWords.sort()

for word in uniqueWords:
    print(word)