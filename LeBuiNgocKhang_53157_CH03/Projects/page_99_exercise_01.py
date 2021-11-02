"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should
indicate whether or not the triangle is an equilateral triangle..

Solution:
Enter length a: 3
Enter length b: 3
Enter length c: 3
The triangle is an enquilateral triangle

Enter length a: 3
Enter length b: 4
Enter length c: 5
The triangle is not an equilateral triangle
"""
# Requests the input
a = int(input("Enter length a: "))
b = int(input("Enter length b: "))
c = int(input("Enter length c: "))
# display the output use if-else
if a == b == c:
    print("The triangle is an enquilateral triangle")
else:
    print("The triangle is not an equilateral triangle")