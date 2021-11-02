"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: The kinetic energy of a moving object is given by the formula KE=(1/2) mv**2 where m is the object’s mass
and v is its velocity. Modify the program you created in Project 5 so that it prints the object’s kinetic energy
as well as its momentum.

Solution:

Enter the object's mass: 1456.777
Enter the object's velocity: 976.11
The object's momentum is:  1421974.5974700002
The object's kinetic energy is:  694001812.1682209

"""
# request the input
mass=float(input("Enter the object's mass: "))
velocity=float(input("Enter the object's velocity: "))
# compute the results
momentum= mass * velocity
kineticEnergy= (mass * velocity ** 2) / 2
# display the results
print("The object's momentum is: ",momentum)
print("The object's kinetic energy is: ",kineticEnergy)
