"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Lightening and darkening are actually special cases of a process known as color
filtering. A color filter is any RGB triple applied to an entire image. The filtering
algorithm adjusts each pixel by the amounts specified in the triple. For example,
you can increase the amount of red in an image by applying a color filter with a
positive red value and green and blue values of 0. The filter (20, 0, 0) would make
an image’s overall color slightly redder. Alternatively, you can reduce the amount
of red by applying a color filter with a negative red value. Once again, the algorithms must avoid exceeding
the limits on the RGB values.
Develop three algorithms for lightening, darkening, and color filtering as three
related Python functions, lighten, darken, and colorFilter. The first two
functions should expect an image and a positive integer as arguments


Solution:

Enter the image file name: dog.gif

"""
from images import Image


def colorFilter(image, rgbTriple):
    """Adds the given rgb values to each pixel after normalizing."""

    def baseValue(value, offset):
        """Normalizes value so that 0 <= value <= 255."""
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = baseValue(r, rgbTriple[0])
            g = baseValue(g, rgbTriple[1])
            b = baseValue(b, rgbTriple[2])
            image.setPixel(x, y, (r, g, b))


def lighten(image, amount):
    """Lightens image by amount."""
    colorFilter(image, (amount, amount, amount))


def darken(image, amount):
    """Darkens image by amount."""
    colorFilter(image, (-amount, -amount, -amount))


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image")
    image.draw()
    lighten(image, 20)
    # darken(image, 20)
    image.draw()


main()
