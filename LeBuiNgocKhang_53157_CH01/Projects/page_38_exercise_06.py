"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:  Write and test a program that computes the area of a circle. This program should request a number
representing a radius as input from the user. It should use the formula 3.14 * radius ** 2 to compute the area and
then output this result suitably labeled.
Solution:
Nhập bán kính R=5
Kết quả: Diện tích hình tròn: 78.5 Circular units.

    ....
"""
radius = float(input(" Enter with R: "))      #   Nhập bán kính R
pi=3.14 #khởi tạo giá trị ban đầu
area=pi*(radius**2) #Tính diện tích hình tròn
print("Diện tích hình tròn:",area, "Circular units.")

