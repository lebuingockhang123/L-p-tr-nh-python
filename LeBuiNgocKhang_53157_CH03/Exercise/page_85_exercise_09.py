"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Does the Boolean expression count > 0 and total // count > 0 contain apotential error? If not, why not?

Solution:

The code contains error.
count >0 This statement is right if we match this with the syntax of regular comparison operation. Here count is
an operand, “0” is the constant operand and these two operands are operated by the operator “>”. when we take
total // count >0 Here count>0 returns Boolean and total is assumed to be an integer and an integer cannot be
divided by a Boolean value. So it can be rectified as (total // count)>0.


"""
