"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: An object’s momentum is its mass multiplied by its velocity. Write a program that accepts an object’s
mass (in kilograms) and velocity (in meters per second) as inputs and then outputs its momentum.

Solution:

Enter the object's mass: 3555.444
Enter the object's velocity: 276.33
The object's momentum is: 982475.84052

"""
# request the input
mass=float(input("Enter the object's mass: "))
velocity=float(input("Enter the object's velocity: "))
# compute the results
momentum= mass * velocity
# display the results
print("The object's momentum is:",momentum)
