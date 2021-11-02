"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of
12%. Monthly payments are 5% of the listed purchase price, minus the down payment. Write a program that takes
the purchase price as input. The program should display a table, with appropriate headers, of a payment schedule
 for the lifetime of the loan. Each row of the table should contain the following items:
• the month number (beginning with 1)
• the current total balance owed
• the interest owed for that month
• the amount of principal owed for that month
• the payment for that month
• the balance remaining after payment
The amount of interest for a month is equal to balance * rate / 12. The amount of
principal for a month is equal to the monthly payment minus the interest owed.


Solution:

Enter the  purchase price: 150
Interest at the end of payment
%0d%20.2f%20.2f%20.2f%13.2f 1 150.0 1.5 6.0 7.5 142.5
%0d%20.2f%20.2f%20.2f%13.2f 2 142.5 1.425 6.075 7.5 135.0
%0d%20.2f%20.2f%20.2f%13.2f 3 135.0 1.35 6.15 7.5 127.5
%0d%20.2f%20.2f%20.2f%13.2f 4 127.5 1.2750000000000001 6.225 7.5 120.0
%0d%20.2f%20.2f%20.2f%13.2f 5 120.0 1.2 6.3 7.5 112.5
%0d%20.2f%20.2f%20.2f%13.2f 6 112.5 1.125 6.375 7.5 105.0
%0d%20.2f%20.2f%20.2f%13.2f 7 105.0 1.05 6.45 7.5 97.5
%0d%20.2f%20.2f%20.2f%13.2f 8 97.5 0.975 6.525 7.5 90.0
%0d%20.2f%20.2f%20.2f%13.2f 9 90.0 0.9 6.6 7.5 82.5
%0d%20.2f%20.2f%20.2f%13.2f 10 82.5 0.8250000000000001 6.675 7.5 75.0
%0d%20.2f%20.2f%20.2f%13.2f 11 75.0 0.75 6.75 7.5 67.5
%0d%20.2f%20.2f%20.2f%13.2f 12 67.5 0.675 6.825 7.5 60.0
%0d%20.2f%20.2f%20.2f%13.2f 13 60.0 0.6 6.9 7.5 52.5
%0d%20.2f%20.2f%20.2f%13.2f 14 52.5 0.525 6.975 7.5 45.0
%0d%20.2f%20.2f%20.2f%13.2f 15 45.0 0.45 7.05 7.5 37.5
%0d%20.2f%20.2f%20.2f%13.2f 16 37.5 0.375 7.125 7.5 30.0
%0d%20.2f%20.2f%20.2f%13.2f 17 30.0 0.3 7.2 7.5 22.5
%0d%20.2f%20.2f%20.2f%13.2f 18 22.5 0.225 7.275 7.5 15.0
%0d%20.2f%20.2f%20.2f%13.2f 19 15.0 0.15 7.35 7.5 7.5
%0d%20.2f%20.2f%20.2f%13.2f 20 7.5 0.075 7.425 7.5 0.0


"""
ANNUAL_RATE = 12/100
MONTHLY_RATE = ANNUAL_RATE / 12

purchase_price = float(input("Enter the  purchase price: "))

monthlyPayment = (5/100) * purchase_price
month = 1
balance = purchase_price
print("Interest at the end of payment")
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interst = 0
    else:
        interst = balance * MONTHLY_RATE
    principal = monthlyPayment - interst
    remaining = balance - monthlyPayment
    print("%0d%20.2f%20.2f%20.2f%13.2f",month, balance, interst, principal, monthlyPayment, remaining)
    balance = remaining
    month += 1


