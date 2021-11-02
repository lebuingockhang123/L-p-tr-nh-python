"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Assume that a file contains integers separated by newlines. Write a code segment that opens the file and
p-oprints the average value of the integers.


Solution:

The average is 38.5

"""
count = 0
sum = 0
inputFile = open("myfile2.txt",'r')
for line in inputFile:
    sum += int(line.strip())
    count += 1
if count == 0:
    average = 0
else:
    average = sum /count
print("The average is", average)



