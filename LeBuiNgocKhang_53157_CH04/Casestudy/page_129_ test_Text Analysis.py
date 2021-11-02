"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Test driver for Flesch Index and Grade level.

Solution:

Sentences: 6
Words: 107
Syllables: 129
Flesch Index: 86.7397741433022
Grade Level:  6

"""
sentences = int(input("Sentences: "))
words = int(input("Words: "))
syllables = int(input("Syllables: "))
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
print("Flesch Index:", index)
level = round(0.39 * (words / sentences) + 11.8 * \
              (syllables / words) - 15.59)
print("Grade Level: ", level)