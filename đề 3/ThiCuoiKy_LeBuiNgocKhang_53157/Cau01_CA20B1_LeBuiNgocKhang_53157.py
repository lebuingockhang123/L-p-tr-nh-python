"""
Đề thi:
Data: 26/10/2021
Author: Lê Bùi Ngọc Kháng

"""

def Cau1():
    def snt(n):
        """ Check so nguyen to """
        f = True
        for j in range(2,n):
            if n % j == 0:
                f = False
                break
        return f
    def in_snt(a=5, b=100):
        print("Danh sach so nguyen to: ")
        """ Kiem tra so nguyen to trong khoang tu a den b """
        for i in range(a, b + 1):
            if snt(i):
                print(i, end=" ")
        print()
    # Thuc thi so nguyen to
    in_snt(5, 100)

if __name__ == '__main__':
    Cau1()