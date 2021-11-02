"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: The functions that draw polygons in the polygons module have the same pattern, varying
only in the number of sides (iterations of the loop). Factor this pattern into a more general
function named polygon, which takes the number of sides as an additional argument.

Solution:
Enter the no of the sides of the polygon : 10
Enter the length of the sides of the polygon : 100

"""
import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))

# taking input for the length of the sides of the polygon
l = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)