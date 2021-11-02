from student import Student

if __name__ == '__main__':

    print(help(Student))

    student_a = Student("Le Bui Ngoc Khang", 5)
    print("Name: ", student_a.getName())
    print("Score: ", student_a.getScore())
    print("Score in i: ", student_a.getScore(2))

    student_a.getScore(1, 9.0)
    print("Score in i: ", student_a.getScore(1))

    print("======="*10)
    print(student_a)