"""
Đề thi:
Data: 26/10/2021
Author: Lê Bùi Ngọc Kháng

"""

# nhập bit đầu vào hệ nhị phân
bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
 decimal = decimal + int(digit) * 2 ** exponent
 exponent = exponent - 1
print("The integer value is", decimal)