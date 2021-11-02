"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,the player wins $4;
otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are lots
of ways to win: (1, 6), (2, 5), and soon. A little mathematical analysis reveals that there are not enough ways
to winto make the game worthwhile; however, because many people’s eyes glaze over at the first mention of
mathematics, your challenge is to write a program that demonstrates the futility of playing the game. Your program
should take as input the amount of money that the player wants to put into the pot, and play the game until the
pot is empty. At that point, the program should print the number of rolls it took to break the player, as well as
maximum amount of money in the pot.


Solution:

Enter dollars: 15
The number of rolls it took to break the player 180 rolls.
quit after 154 rolls when you had $16.

"""
import  random
# request the input
dollars = int(input("Enter dollars: "))

# initialize variables
maximum_amount = dollars
countMax = 0
count = 0
# loop until the money is gone
while dollars > 0:
    count += 1
    # roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # calculate the winnings or losses
    if dice1 + dice2 == 7:
        dollars += 4
    else:
        dollars -= 1
        # if this is a new maximum, remember it
        if dollars > maximum_amount:
            maxdollars = dollars
            countMax = count
# display the results
print("The number of rolls it took to break the player " + str(count) + " rolls.\n" +
      "quit after " + str(countMax) + " rolls when you had $" + str(maxdollars) + ".")




