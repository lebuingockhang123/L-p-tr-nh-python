"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:
    The edge-detection function described in this chapter returns a black-and-white
image. Think of a similar way to transform color values so that the new image is still
in its original colors but the outlines within it are merely sharpened. Then, define a
function named sharpen that performs this operation. The function should expect
an image and two integers as arguments. One integer should represent the degree
to which the image should be sharpened. The other integer should represent the
threshold used to detect edges

Solution:

Enter the image file name: dog.gif

"""
from images import Image


def sharpen(image, degree, threshold):
    """Builds and returns a sharpened image.  Expects an image
    and two integers (the degree to which the image should be sharpened and the
    threshold used to detect edges) as arguments."""

    def average(triple):
        """Returns the average of the values in the tuple."""
        (r, g, b) = triple
        return (r + g + b) // 3

    new = image.clone()  # Make changes to a copy
    for y in range(image.getHeight() - 1):  # Work inside the borders
        for x in range(1, image.getWidth()):
            # Obtain average values of current, left, and
            # bottom pixels
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            # Detect an edge at current pixel
            if abs(oldLum - leftLum) > threshold or \
                    abs(oldLum - bottomLum) > threshold:
                # Darken that edge
                new.setPixel(x, y,
                             (max(oldPixel[0] - degree, 0),
                              max(oldPixel[1] - degree, 0),
                              max(oldPixel[2] - degree, 0)))
    return new


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image.")
    image.draw()
    newimage = sharpen(image, 20, 15)
    newimage.draw()


main()
