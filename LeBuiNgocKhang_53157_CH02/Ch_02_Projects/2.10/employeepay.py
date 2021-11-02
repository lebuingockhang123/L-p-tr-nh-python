"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus
any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a
program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an
employee’s total weekly pay.

Solution:

Enter the wage: $ 20
Enter the regular hours: 40
Enter the overtime hours:  15
The total weekly pay is $ 1250.0

"""
# request the input
hourlyWages=float(input("Enter the wage: $ "))
totalRegularHours=float(input("Enter the regular hours: "))
overtimeHours=float(input("Enter the overtime hours:  "))
# compute the result
totalEmployeePay= hourlyWages * totalRegularHours + overtimeHours * hourlyWages * 1.5
# display the result
print("The total weekly pay is $ " + str(round(totalEmployeePay, 2)))
