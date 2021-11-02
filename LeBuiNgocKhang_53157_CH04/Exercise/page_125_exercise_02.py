"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a code segment that opens a file for input and prints the number of four-letter words in the file.


Solution:

There are 2 lines.

"""
count = 0
inputFile = open("myfile.txt", 'r')
for line in inputFile:
    wordlist = line.split()
    for word in wordlist:
        if len(word) == 4:
            count += 1
print("There are", count, "lines.")