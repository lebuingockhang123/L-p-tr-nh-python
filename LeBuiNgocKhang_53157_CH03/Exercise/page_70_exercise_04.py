"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a loop that prints the first 128 ASCII values followed by the corresponding characters (see the
section on characters in Chapter 2). Be aware that most of the ASCII values in the range “0..31” belong to special
control characters with no standard print representation,so you might see strange symbols in the output for these
values.

Solution:


"""

#Displays ASCII Table
for asciiLoop in range(128):
    print(" " +str(asciiLoop) + "   " + chr(asciiLoop))