"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should
indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides.

Solution:

Enter length a: 3
Enter length b: 4
Enter length c: 5
The triangle is a right triangle

Enter length a: 2
Enter length b: 3
Enter length c: 4
The triangle is not a right triangle


"""
# Requests the input
a = int(input("Enter length a: "))
b = int(input("Enter length b: "))
c = int(input("Enter length c: "))
# compute the squares
square1 = a ** 2
square2 = b ** 2
square3 = c ** 2
# Check condition and print ringt triangle or normal triangle
if square1 + square2 == square3 or square2 + square3 == square1 or square1 + square3 == square2:
    print("The triangle is a right triangle")
else:
    print("The triangle is not a right triangle")