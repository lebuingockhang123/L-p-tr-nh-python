"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that computes the Flesch Index and grade level for text stored in a text file.


Solution:
Step 1: Analysis
 Input: Enter "text file". Output display index,level,sentences,words,syllables
 Compute: + index F :
 F = 206.835 - 1.015 × ( words/sentences) − 84.6 * (syllables / words)
           + Level G
G = 0.39 * (words/sentences) + 11.8 * (syllables/words) − 15.59
Step 2: Design
This program will perform the following tasks:
1. Receive the filename from the user, open the file for input, and input the text.
2. Count the sentences in the text.
3. Count the words in the text.
4. Count the syllables in the text.
5. Compute the Flesch Index.
6. Compute the Grade Level Equivalent.
7. Print these two values with the appropriate labels, as well as the counts from
tasks 2–4.
Step 3: Implementation
The main tasks are marked off in the program code with a blank line and a comment
Step 4: Testing
 Although the main tasks all collaborate in the text analysis program, they can be tested more or less independently,
before the entire program is tested. After all, there is no point in running the complete program if you are
unsure that even one of the tasks does not work correctly
      ----------------------------------------------------------------
    Results:
The Flesch Index is 86.7397741433022
The Grade Level Equivalent is 6
6 sentences
107 words
129 syllables

"""
# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
# Count the sentences
sentences = text.count('.') + text.count('?') + \
 text.count(':') + text.count(';') + \
 text.count('!')
# Count the words
words = len(text.split())
# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
           syllables -= 1
    if word.endswith('le'):
       syllables += 1
# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * \
        (syllables / words) - 15.59)
# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")