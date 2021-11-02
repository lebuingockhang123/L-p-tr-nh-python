"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem:Open an IDLE window, and enter the program from Figure 1-7 that computes the area of a rectangle. Load the
program into the shell by pressing the F5 key, and correct any errors that occur. Test the program with different
inputs by running it at least three times.
Solution:
    STEP 1: Chaỵ IDLE
    STEP 2: Nhấn vào tab file và sau đó chọn New file, xuất hiện 1 cửa sổ không có tiêu đề.
    STEP 3: Nhập chương trình từ Figure 1-7 vào cửa sổ
    STEP 4: Nhấn F5 để thực thi tập lệnh python
    STEP 5: Trước khi hiển thị đầu ra, màn hình xuất hiện hộp thoại "Source Must Be Saved. OK to Save?". Nhấn OK để
tiếp tục
    STEP 6: Lưu thư mục tên page_38_exercise_04.py
    STEP 7: Cửa sổ python shell sẽ hiển thị đầu ra cho tập tin
    STEP 8: Nhập width và height là: 3 và 4.Hiển thị kết quả:The area is 12 square units.
    STEP 9: Quay lại cửa sổ ở STEP 3 ấn F5. Thực hiện STEP 8: Nhập 5 và 9. Kêt quả: The area is 45 square units.
Tương tự Nhập 9 và 15. Kết quả:  The area is 135 square units.
    ....
"""
width = int(input(" Enter with width: "))
height =int(input(" Enter with height: "))
area = width * height
print(" The area is", area,"square units.")
