"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Old-fashioned photographs from the nineteenth century are not quite black and
white and not quite color, but seem to have shades of gray, brown, and blue. This
effect is known as sepia,
Write and test a function named sepia that converts a color image to sepia. This
function should first call grayscale to convert the color image to grayscale. A
code segment for transforming the grayscale values to achieve a sepia effect follows.

Solution:

Enter the image file name: dog.gif

"""
from images import Image


def sepia(image):
    """Converts an image to sepia."""
    grayscale(image)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            image.setPixel(x, y, (r, g, b))


def grayscale(image):
    """Converts an image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


if __name__ == '__main__':

    filename = input("Enter the image file name: ")
    image = Image(filename)
    sepia(image)
    image.draw()