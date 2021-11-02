"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Evaluate the following code at a shell prompt: print ("Your name is", name). Then assign name an appropriate
value, and evaluate the statement again
Solution:
    Hàm print ("Your name is", name) là một hàm lỗi sai cú pháp vì sau print là đối tượng cần in là đúng và sau dấu
phẩy là đối tượng chỉ định được phân tách thành phần nhỏ bằng ký tự được phân tách trước khi được in và giá trị này
mặc định là 1 khoảng trắng ' '. Sau đây là đoạn code mô phỏng:
        ....
"""
print("Tôi tên là:",'Lê Bùi Ngọc Kháng')
