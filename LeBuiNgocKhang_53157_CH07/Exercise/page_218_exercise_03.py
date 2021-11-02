"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Add a function named circle to the polygons module. This function expects the same arguments as the square
and hexagon functions. The function should draw a circle. (Hint: the loop iterates 360 times.)

Solution:


"""

import turtle

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360 / n)

bob = turtle.Turtle()

bob.penup()
bob.sety(-270)
bob.pendown()
polygon(bob, 30, 60)
turtle.mainloop()



