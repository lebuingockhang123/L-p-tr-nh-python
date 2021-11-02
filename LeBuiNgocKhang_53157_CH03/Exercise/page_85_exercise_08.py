"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  The variables x and y refer to numbers. Write a code segment that prompts the user for
an arithmetic operator and prints the value obtained by applying that operator to x and y


Solution:
Enter the value of x: 4
Enter the value of y: 8
Enter an arithmetic operator: *
32

Enter the value of x: 33
Enter the value of y: 11
Enter an arithmetic operator: /
3.0

Enter the value of x: 4
Enter the value of y: 5
Enter an arithmetic operator: =
Invalid Charater!


"""
# request the input
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
op = input("Enter an arithmetic operator: ")
# use condition to display operator
if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
elif op == "%":
    print(x % y)
else:
    print("Invalid Charater!")