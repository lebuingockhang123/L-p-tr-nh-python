"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Modify the guessing-game program of Section 3.5 so that the user thinks of a number that the computer
 must guess. The computer must make no more than the minimum number of guesses, and it must prevent the user from
cheating by entering misleading hints. (Hint: Use the math.log function to compute the minimum number of guesses
needed after the lower and upper bounds are entered.)

Solution:

Enter the smaller number: 3
Enter the larger number: 8
38
Your name is 5
Enter =, <, or >:<
34
Your name is 3
Enter =, <, or >:=
Congratulations!, You've got it in 2 tries!

"""

import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print("my name is %d" %myNumber)
    guess = input("Enter =, <, or >:")
    if guess == "=":
        print("Congratulations!, You've got it in", count, "tries!")
        break
    elif guess == ">":
        larger = myNumber + 1
    else:
        smaller = myNumber - 1

 
