"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Describe the processes of top-down design and stepwise refinement. Where does
the design start, and how does it proceed?

Solution:


"""
# Chapter 04 includes length, binary_to_decimal, decimal_to_binary
def length():
    enter = input("Enter number to calculate length: ")
    print(f"Length of {enter} is {len(enter)}")


def binary_to_decimal():
    bitString = input("Enter a string of bits: ")
    decimal = 0
    exponent = len(bitString) - 1
    for digit in bitString:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent - 1
    print("The integer value is", decimal)


def decimal_to_binary():
    decimal = int(input("Enter a decimal integer: "))
    if decimal == 0:
        print(0)
    else:
        # print("Quotient Remainder Binary")
        bitString = ""
        while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            bitString = str(remainder) + bitString
            print("%5d%8d%12s" % (decimal, remainder, bitString))
    print("The binary representation is", bitString)


# Chapter_05 include odd and even
def odd():
    x = int(input("Enter number to check odd: "))
    """ Print the result"""
    if x % 2 == 1:
        print(f"{x} is an odd")
    else:
        print(f"{x} is not an odd")


def even():
    x = int(input("Enter number to check even: "))
    """ Print the result"""
    if x % 2 == 0:
        print(f"{x} is an even")
    else:
        print(f"{x} is not an even")


def chapter_04():
    ans = True
    while ans:
        print(""""
            1. Print length
            2. Convert binary to decimal
            3. Convert decimal to binary
            4.Exit/Quit
            """"")
        ans = input("Choose number: ")
        if ans == "1":
            length()
        elif ans == "2":
            binary_to_decimal()
        elif ans == "3":
            decimal_to_binary()
        elif ans == "4":
            ans = False
        elif ans != "":
            print("\n Not Valid Choice Try again")


def chapter_05():
    ans = True
    while ans:
        print("""
            1. Check a number is an odd or no?
            2. Check a number is an even or no?
            3.Exit/Quit
            """)
        ans = input("Choose number: ")
        if ans == "1":
            odd()
        elif ans == "2":
            even()
        elif ans == "3":
            ans = False
        elif ans != "":
            print("\n Not Valid Choice Try again")


def main():
    ans = True
    while ans:
        print("""
        1. Choose chapter 04
        2. Choose chapter 05
        3.Exit/Quit
        """)
        ans = input("Choose number: ")
        if ans == "1":
            chapter_04()
        elif ans == "2":
            chapter_05()
        elif ans == "3":
            ans = False
        elif ans != "":
            print("\n Not Valid Choice Try again")


if __name__ == '__main__':
    main()