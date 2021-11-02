"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that takes the radius of a sphere (a floating-point number) as input and then outputs the
 sphere’s diameter, circumference, surface area, and volume

Solution:

Enter the sphere's radius: 35
Diameter:  70.0
Circumference:  219.9114857512855
surfaceArea:  15393.804002589986
Volume:  179594.38003021647

"""

import math

# Request the input
radius= float(input("Enter the sphere's radius: "))
# Compute the results
diameter= radius * 2
circumference= diameter * math.pi
surfaceArea= 4 * math.pi * radius * radius
volume= 4 / 3.0 * math.pi * radius * radius * radius
# display the results
print("Diameter: ",diameter)
print("Circumference: ",circumference)
print("surfaceArea: ",surfaceArea)
print("Volume: ",volume)
