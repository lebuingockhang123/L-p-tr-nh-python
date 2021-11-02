"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Explain what goes on behind the scenes when your computer runs a Python program.
Solution:
   - The interpreter reads the statements and check for syntactical errors. If found any error then it halts the
process and return the error message.
   -  If a Python expression is well formed, the interpreter then translates it to an equivalent form in a low-level
language called byte code.
   - This byte code is next sent to another software component, called the Python virtual machine (PVM), where it is
executed. If another error occurs during this step, execution also halts with an error message.
   - If no error found by PVM then it gives the final output.
    ....
"""