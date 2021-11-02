"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  A local biologist needs a program to predict population growth. The inputs would be the initial number
of organisms, the rate of growth (a real number greater than 0), the number of hours it takes to achieve this rate, and a number
of hours during which the population grows. For example, one might start with a population of 500 organisms, a
growth rate of 2, and a growth period to achieve this rate of 6 hours. Assuming that none of the organisms die,
this would imply that this population would double in size every 6 hours. Thus, after allowing 6 hours for growth,
we would have 1000 organisms, and after 12 hours, we would have 2000 organisms. Write a program that takes these
inputs and displays a prediction of the total population.


Solution:

Enter the initial number of organisms: 1500
Enter the rate of growth: 1.5
Enter the number of hours to achieve the rate of growth: 5
Enter the total hours of growth: 15
The total is population is:  5062

"""
# request the input
initial_population = int(input("Enter the initial number of organisms: "))
rate = float(input("Enter the rate of growth: "))
cyclehours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalhours = int(input("Enter the total hours of growth: "))
# caculate the number of cycles
cycles = totalhours // cyclehours
# caculate the population
for i in range(cycles):
    initial_population = initial_population * rate
# displays the total population
print("The total is population is: ",int(initial_population))
