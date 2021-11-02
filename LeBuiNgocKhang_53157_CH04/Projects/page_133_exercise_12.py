"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: The Payroll Department keeps a list of employee information for each pay period in a text file. The
format of each line of the file is the following:
<last name> <hourly wage> <hours worked>
Write a program that inputs a filename from the user and prints to the terminal a report of the wages paid to the
employees for the given period. The report should be in tabular format with the appropriate header. Each line
should contain an employee’s name, the hours worked, and the wages paid for that period.

Solution:

Enter the file name: test12.txt
Name            Hours      Total Pay
John               26         196.56
Peter              22         104.50
David              11          35.42
Ronaldo             3           0.45
Messi               3           0.51


"""
# take the input
fileName = input("Enter the file name: ")
# open the input file
inputFile = open(fileName, 'r')
# read the data and print the report
print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split()
    name = dataList[0]
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours * payRate
    print("%-15s%6d%15.2f" % (name, hours, totalPay))