"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:Enter an input statement using the input function at the shell prompt. When the prompt asks you for input,
enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened
Solution:
  Giải thích kết quả: Điều này gây ra lỗi tại dòng n = n + 1 vì không thể chuyển đổi hoàn toàn đối tượng
int thành str
    ....
"""
n = input('Enter a Number: ')
n = n + 1
print(n)