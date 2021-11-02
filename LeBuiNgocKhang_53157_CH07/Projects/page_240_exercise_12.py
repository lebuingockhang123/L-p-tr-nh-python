"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:
    Each image-processing function that modifies its image argument has the same
loop pattern for traversing the image. The only thing that varies is the code used
to change each pixel within the loop. Section 6.6 of this book, on higher-order
functions, suggests a simpler design pattern for such code. Design a single function,
named transform, which expects an image and a function as arguments.
When this function is called, it should be passed another function that expects a
tuple of integers and returns a tuple of integers. This is the function that transforms the information
for an individual pixel (such as converting it to black and
white or gray-scale). The transform function contains the loop logic for traversing its image argument.
In the body of the loop, the transform function accesses
the pixel at the current position, passes it as an argument to the other function,
and resets the pixel in the image to the function’s value. Write and test a script
that defines this function and uses it to perform at least two different types of
transformation on an image

Solution:

Enter the image file name: dog.gif

"""
from images import Image


def transform(image, function):
    """Traverses the image and resets each pixel with the result
    of applying the function to it."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            image.setPixel(x, y, function(image.getPixel(x, y)))


def grayscale(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""

    def change(triple):
        """Converts a pixel to grayscale."""
        (r, g, b) = triple
        r = int(r * 0.299)
        g = int(g * 0.587)
        b = int(b * 0.114)
        lum = r + g + b
        return (lum, lum, lum)

    transform(image, change)


def blackAndWhite(image):
    """Converts an image to black and white."""

    def change(triple):
        """Converts a pixel to black and white."""
        (r, g, b) = triple
        average = (r + g + b) // 3
        if average < 128:
            return (0, 0, 0)
        else:
            return (255, 255, 255)

    transform(image, change)


if __name__ == '__main__':
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale(image)
    # blackAndWhite(image)
    image.draw()

