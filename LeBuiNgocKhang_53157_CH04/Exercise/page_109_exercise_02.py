"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Consult the Table of ASCII values in Chapter 2 and suggest how you would modify the encryption and
decryption scripts in this section to work with strings containing all of the printable characters.

Solution:

  I would have to do is write a program that would run the same line of text through the extended decrypt script
with the values 0 through 127, until a meaningful plaintext is returned. It would take less than a second to do
that on most modern computers. The main shortcoming of this encryption strategy is that the plaintext is encrypted
one character at a time, and each encrypted character depends on that single character and a fixed distance value.

"""
