"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a program that receives a series of numbers from the user and allows the user to press the enter
 key to indicate that he or she is finished providing inputs. After the user presses the enter key, the program
 should print the sum of the numbers and their average


Solution:

Enter a number: 4
Enter the next number: 5
Enter the next number: 2
Enter the next number:
The sum is 11.0
The average is: 3.67

"""
theSum = 0
count = 0
data = input("Enter a number: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter the next number: ")
    count += 1
print("The sum is", theSum)
if count > 0:
    avg = theSum / count
    print("The average is: " + str(round(avg,2)))


