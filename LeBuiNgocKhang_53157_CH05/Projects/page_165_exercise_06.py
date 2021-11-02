"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases

Solution:
10
12
1010
A


"""

repTable = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 14: 'D', 15: 'E', 16: 'F'
}


def decimalToRep(decimal, base):
    if decimal == 0:
        return '0'
    else:
        rep = ""
        while decimal > 0:
            remainder = decimal % base
            decimal = decimal // base
            rep = repTable[remainder] + rep
        return rep


def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))


if __name__ == '__main__':
    main()
