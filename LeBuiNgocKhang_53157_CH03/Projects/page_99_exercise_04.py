"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: A standard science experiment is to drop a ball and see how high it bounces. Once the “bounciness” of the
ball has been determined, the ratio gives a bounciness index. For example, if a ball dropped from a height of 10 feet
bounces 6 feet high, the index is 0.6, and the total distance traveled by the ball is 16 feet after one bounce. If
the ball were to continue bouncing, the distance after two bounces would be 10ft + 6ft + 6ft + 3.6ft = 25.6 ft.
Note that the distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance
as the ball comes back up. Write a program that lets the user enter the initial height from which the ball is dropped
and the number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the
ball.

Solution:

Enter the height from which the ball is dropped: 40
Enter the bounciness index of the ball: 4
Enter the number of times the ball is allowed to continue bouncing: 2
Total distance traveled is: 1000.0 units.

"""
# request the input
height = float(input("Enter the height from which the ball is dropped: "))
bounce_index = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
#  Initialize the distance
distance = 0
# perform calculations
for i in range(bounces):
    distance += height
    height *= bounce_index
    distance += height
# display the distance
print("Total distance traveled is:",distance,"units.")

