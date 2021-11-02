"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program: What is a mutator method? Explain why mutator methods usually return the value None.

Solution:
  In computer science, a mutator method is a method used to control changes to a variable. They are also widely
known as setter methods. Often a setter is accompanied by a getter (also known as an accessor), which returns the
value of the private member variable.
  Because a change of state is all that is desired, a mutator method usually returns no value of interest to the
caller (but note that pop is an exception to this rule). Python nevertheless automatically returns the special
value None even when a method does not explicitly return a value.

"""
