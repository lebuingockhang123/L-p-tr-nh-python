"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: The Turtle class includes a method named circle. Import the Turtle class, run
help(Turtle.circle), and study the documentation. Then use this method to
draw a filled circle and a half moon.

Solution:


"""
import turtle

turtle.Screen()
turtle.bgcolor("magenta")

turtle.color("yellow")
turtle.begin_fill()
turtle.circle(130, 180)
turtle.end_fill()
turtle.hideturtle()