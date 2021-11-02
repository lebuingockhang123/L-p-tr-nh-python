"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write an algorithm that describes the second part of the process of making change.
Solution:
    Step 1: Take the total amount and take variables for quarter,dime and penny and initialize them to zero
    Step 2: If total amount >=15 divide it by 15 and add 1 to quarter. Repeat the process until it is false.
    Step 3: If total amount >=10 divide it by 10 and add 1 to dime. Repeat the process until it is false.
    Step 4: Add total amount to penny.
    Step 5: Number of quarter, dime and penny are the required changes.
    ....
"""