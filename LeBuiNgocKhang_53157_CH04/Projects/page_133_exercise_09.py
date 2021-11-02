"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a script named copyfile.py. This script should prompt the user for the names of two text files.
The contents of the first file should be input and written to the second file.

Solution:

Enter the input file name: test9.txt
Enter the output file name: test9_output
This script creates a program listing from a

source program. This script should prompt the user for the names of two files. The

input filename could be the name of the script itself, but be careful to use a different

output filename!


"""
# request the input
inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")
# open the input file and read the text
outfile = open(outputFile, "w")
# open the input files
with open(inputFile, 'r') as file:
    index = 1
    for line in file:
        print(line)
        outfile.write("%d>"%index + line)
        index += 1
outfile.close()