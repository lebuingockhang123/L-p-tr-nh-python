"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Modify this chapter’s case study program (the c-curve) so that it draws the line
segments using random colors.


Solution:

Please enter the number of levels: 10

"""
from turtle import *

def line(t, x1, y1, x2, y2):
    """draws the line segment from x1,y1 to x2,y2"""

    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

def drawLine(t, x1, y1, x2, y2, level):
    """forms the shape"""

    if level == 0:
        line(t, x1, y1, x2, y2)
    else:
        xm = ((x1 + x2) + (y2 - y1)) // 2
        ym = ((y1 + y2) + (x1 - x2)) // 2
        drawLine(t, x1, y1, xm, ym, level-1)
        drawLine(t, xm, ym, x2, y2, level-1)

def main():
    """the main function"""

    myTurtle = Turtle()

    myTurtle.hideturtle()

    num = int(input("Please enter the number of levels: "))

    drawLine(myTurtle, 100, 0, 100, -200, num)


main()