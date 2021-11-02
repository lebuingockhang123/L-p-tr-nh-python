"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Define a second version of the grayscale function that uses the allegedly crude
method of simply averaging each RGB value. Test the function by comparing its
results with those of the other version discussed in this chapter.


Solution:

Enter the image file name: dog.gif

"""
from images import Image


def grayscale1(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


def grayscale2(image):
    """Converts an image to grayscale using the crude average
    of the r, g, and b"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            ave = (r + g + b) // 3
            image.setPixel(x, y, (ave, ave, ave))


if __name__ == '__main__':
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale2(image)
    image.draw()
