"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a program that generates sentences.

Solution:
Generates and displays sentences using a simple grammar and vocabulary. Words are chosen at random
Enter the number of sentences: 3
THE BOY HIT THE BOY BY A BALL
A BOY HIT THE GIRL WITH THE BALL
A BALL LIKED A GIRL WITH THE BOY

"""
import random

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")

def sentence():
     """Builds and returns a sentence."""
     return nounPhrase() + " " + verbPhrase()

def nounPhrase():
     """Builds and returns a noun phrase."""
     return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
     """Builds and returns a verb phrase."""
     return random.choice(verbs) + " " + nounPhrase() + " " + \
            prepositionalPhrase()
def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
 # The entry point for program execution
if __name__ == "__main__":
    main()