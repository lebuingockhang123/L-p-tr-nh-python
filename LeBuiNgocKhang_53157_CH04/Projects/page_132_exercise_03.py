"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text

Solution:
+ encrypt text
Enter the input file name: test.txt
Enter the output file name:  test_encrypted
Enter the distance value: 3
code: P|#qdph#lv#Nkdqj
+ decrypt text
Enter the input file name: test_encrypted
Enter the output file name: test_decrypted
Enter the distance value: 3
code: My name is Khang

"""
inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))
infile = open(inputFile, "r")
outfile = open(outputFile, "w")
data = infile.readlines()
# encrypted txt
for text in data:
    code = ""
    for char in text:
        Value = ord(char)
        cipher = Value + distance
        if(cipher > 127):
            cipher = distance - (127 - Value + 1)
        code += chr (cipher)
print(f"code: {code}")
outfile.write(code)
outfile.close()

# decrypted text

inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))
infile = open(inputFile, "r")
outfile = open(outputFile, "w")
data = infile.readlines()
for text in data:
    code = ""
    for char in text:
        Value = ord(char)
        cipher = Value - distance
        if cipher < 0:
            cipher = 127 - (distance - (1- value))
        code += chr(cipher)
print(f"code: {code}")
outfile.write(code)
outfile.close()