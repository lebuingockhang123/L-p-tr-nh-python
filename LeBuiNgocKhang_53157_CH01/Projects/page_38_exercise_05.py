"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:   Modify the program of Project 4 to compute the area of a triangle. Issue the appropriate prompts for the
triangle’s base and height, and change the names of the variables appropriately. Then, use the formula
5 * base * height to compute the area. Test the program from an IDLE wind.
Solution:
 Tương tự như solution ở page_38_exercise.Nhập a=3, height=4 Kết quả hiển thị:The area is 6.0  square units.
    ....
"""
width = int(input(" Enter with a: "))  # nhap base = a
height =int(input(" Enter with height: ")) # nhap chieu rong
area = 0.5* width * height #tính dien tinh
print(" The area is", area,"square units.")