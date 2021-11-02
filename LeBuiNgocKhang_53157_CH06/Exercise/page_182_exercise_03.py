"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: Describe the costs and benefits of defining and using a recursive function

Solution:
- Cost:
    + When a call returns or completes its execution, the return address is used to locate the next instruction
in the caller’s code, and the memory for the stack frame is deallocated.
- Benefit:
    + It uses system stack to accomplish it's task. As stack uses LIFO approach and when a function is called the
controlled is moved to where function is defined which has it is stored in memory with some address, this address
is stored in stack.
    + It reduces a time complexity of a program.

"""