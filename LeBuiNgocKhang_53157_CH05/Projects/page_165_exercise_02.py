"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number

Solution:

Enter the file name: enter_file
The number of lines in this txt. file is 2
Please enter a line number or press 0 to quit: 1
my name is khÃ¡ng


"""

enter_file = input("Enter the file name: ")
file = open(enter_file, 'r')
line_count = 0

for line in file:
    line_count = line_count + 1

print("The number of lines in this txt. file is", line_count)

while True:
    line_num = 0

    num = int(input("Please enter a line number or press 0 to quit: "))
    if 1 <= num <= line_count:
        file = open(enter_file, 'r')
        for lines in file:
            line_num = line_num + 1
            if line_num == num:
                print(lines)
    else:
        if num == 0:
            print("Thanks for using the program")
            break