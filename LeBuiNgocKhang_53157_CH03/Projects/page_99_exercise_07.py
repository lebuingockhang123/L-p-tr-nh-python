"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Teachers in most school districts are paid on a schedule that provides a salary based on their number
of years of teaching experience. For example, a beginning teacher in the Lexington School District might be paid
$30,000 the first year. For each year of experience after this first year, up to 10 years, the teacher receives a
2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for
teachers in a school district. The inputs are the starting salary, the percentage increase, and the number of years
 in the schedule. Each row in the schedule should contain the year number and the salary for that year.


Solution:

Enter the starting salary: $ 35000
Enter the annual % increase: 3
Enter the year number: 5
The salary schedule is: 35000.0
The salary schedule is: 36050.0
The salary schedule is: 37131.5
The salary schedule is: 38245.44
The salary schedule is: 39392.81

"""
# request the input
start_salary = float(input("Enter the starting salary: $ "))
increase = int(input("Enter the annual % increase: "))
year = int(input("Enter the year number: "))
# compute the input
multiplier = 1 + increase / 100
next_salary = start_salary
for year in range(1, year + 1):
    print("The salary schedule is: " + str(round(next_salary,2)))
    next_salary *= multiplier
