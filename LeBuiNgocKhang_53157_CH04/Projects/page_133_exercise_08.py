"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a script named copyfile.py. This script should prompt the user for the names of two text files.
The contents of the first file should be input and written to the second file.

Solution:

Enter the input file name: test8.txt
Enter the output file name: test8_output
code: hi. my name is Khang
I love my sport

"""
# request the input
inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")
# open the input file and read the text
infile = open(inputFile, "r")
text = infile.read()
# open the output file and write the text
outfile = open(outputFile, 'w')
print(f"code: {text}")
outfile.write(text)
outfile.close()