"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Why does the blur function need to work with a copy of the original image?

Solution:
   When processing an image, we are often interested in identifying objects represented within it so that we can
perform some further analysis of these objects e.g. by counting them, measuring their sizes, etc. An important
concept associated with the identification of objects in an image is that of edges: the lines that represent a
transition from one group of similar pixels in the image to another different group. One example of an edge is
the pixels that represent the boundaries of an object in an image, where the background of the image ends and the
object begins.



"""