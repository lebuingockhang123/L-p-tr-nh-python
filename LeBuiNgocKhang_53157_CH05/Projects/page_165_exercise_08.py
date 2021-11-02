"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:   A file concordance tracks the unique words in a file and their frequencies. Write
a program that displays a concordance for a file. The program should output the
unique words and their frequencies in alphabetical order. Variations are to track
sequences of two words and their frequencies, or n words and their frequencies.

Solution:

Word            Frequency
ARE            : 1
DOING          : 1
WHAT           : 1
YOU            : 1


"""


f = " WHAT ARE YOU DOING?"
myDict = {}
line_num = 0

for word in f.split():
    if not word in myDict:
        myDict[word] = []

    myDict[word].append(line_num)

print("%-15s %-15s" % ("Word", "Frequency"))
for key in sorted(myDict):
    print('%-15s: %-15d' % (key, len(myDict[key])))