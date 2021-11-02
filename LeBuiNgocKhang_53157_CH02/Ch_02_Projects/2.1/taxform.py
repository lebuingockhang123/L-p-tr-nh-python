"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: The tax calculator program of the case study outputs a floating-point number that might show more than two
digits of precision. Use the round function to modify the program to display at most two digits of precision in the
output number.

Solution:
   Enter:
Enter the gross income: 34520
Enter the number of dependents: 2
The income tax is $3704.0

Enter the gross income: 135.467
Enter the number of dependents: 2
The income tax is $-3172.91

     """
# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
 DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(round(incomeTax, 2)))