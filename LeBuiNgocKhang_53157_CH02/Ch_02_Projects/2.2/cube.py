"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: You can calculate the surface area of a cube if you know the length of an edge. Write a program that takes
the length of an edge (an integer) as input and prints the cube’s surface area as output.

Solution:
Enter the edge of the cube: 6
The surface area is: 216.0 square unit.

"""

# request the input
edge =float(input("Enter the edge of the cube: "))
#compute the surface area
surfaceArea=6*edge*edge
# display the surface area
print("The surface area is:",surfaceArea, "square unit.")
