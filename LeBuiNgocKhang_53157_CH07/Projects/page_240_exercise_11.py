"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:
    To enlarge an image, one must fill in new rows and columns with color
information based on the colors of neighboring positions in the original image.
Develop and test a function named enlarge. This function should expect an
image and an integer factor as arguments. The function should build and return
a new image that represents the expansion of the original image by the factor


Solution:

Enter the image file name: dog.gif

"""
from images import Image


def enlarge(image, factor):
    """Builds and returns a copy of the image which is larger
    by the factor."""
    oldWidth = image.getWidth()
    oldHeight = image.getHeight()
    new = Image(oldWidth * factor, oldHeight * factor)
    oldY = 0
    newY = 0
    while oldY < oldHeight:
        for countY in range(factor):
            oldLeft = 0
            oldRight = oldWidth - 1
            newLeft = 0
            newRight = new.getWidth() - 1
            while oldLeft < oldRight:
                leftPixel = image.getPixel(oldLeft, oldY)
                rightPixel = image.getPixel(oldRight, oldY)
                for count in range(factor):
                    new.setPixel(newLeft, newY, leftPixel)
                    new.setPixel(newRight, newY, rightPixel)
                    newLeft += 1
                    newRight -= 1
                oldLeft += 1
                oldRight -= 1
            newY += 1
        oldY += 1
    return new


if __name__ == '__main__':

    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image.")
    image.draw()
    newimage = enlarge(image, 2)
    newimage.draw()

