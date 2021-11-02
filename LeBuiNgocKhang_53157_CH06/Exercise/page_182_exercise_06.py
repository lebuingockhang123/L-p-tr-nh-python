"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Explain what happens when the following recursive function is called with the values "hello" and 0 as arguments:
def example(aString, index):
   if index < len(aString):
     example(aString, index + 1)
     print(aString[index], end = "")

Solution:
 - len("hello") = 5. 0 < 5 => Program run until index = 5 which stops.
    - 1. aString[0] = "h"
    - 2. aString[1] = "e"
    - 3. aString[2] = "l"
    - 4. aString[3] = "l"
    - 5. aString[4] = "o"
    - Program runs and print from 1-2-3-4-5 => result is: "olleh"

"""
def example(aString, index):
    if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end="")


example("hello", 0)