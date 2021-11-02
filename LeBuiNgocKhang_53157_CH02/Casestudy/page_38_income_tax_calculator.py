"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: The customer requests a program that computes a person’s income tax.
Solution:
   Bước: Phân tích:
   - Tât cả những người nộp thuế đều chịu 20%.
   - All người đóng thuể được chiết khấu tiêu chuẩn 10,000$
   - Đối với mỗi người phụ thuộc, người đóng thuế được phép khấu trừ thêm 3,000$
   - Tổng thu nhập được nhập chính xác và Thuế thu nhập được biểu thị dưới dạng số thập phân
   Bước: Thiết kế:
   - Nhập tổng thu nhập và số người phụ thuộc
   - Tính thu nhập chịu thuế theo công thức
   - Thu nhập chịu thuế = tổng thu nhập - 10000 - (3000 * số người phụ thuộc)
   -Tính thuế thu nhập bằng công thức : Thuế = thu nhập chịu thuế * 0,20
   - In thuế
   Bước : viết chương trình và test
  Ví dụ : Open IDLE. Viết chương trình tính tổng thuế bên dưới.ENTER :
    - grossIncome=10000, numDependents=0. Result: The income tax is $0.0
    - grossIncome=10000, numDependents=1. Result: The income tax is $-600.0
    - grossIncome=10000, numDependents=2. Result: The income tax is $-1200.0
    - grossIncome=20000, numDependents=0. Result: The income tax is $2000.0
    - grossIncome=20000, numDependents=1. Result: The income tax is $1400.0
    - grossIncome=20000, numDependents=2. Result: The income tax is $800.0
    ....
"""
# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
 DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(incomeTax))