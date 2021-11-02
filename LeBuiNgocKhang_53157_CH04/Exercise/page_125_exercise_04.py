"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Problem: Write a code segment that prints the names of all of the items in the current working directory.


Solution:
myfile.txt
myfile2.txt
page_106_exercise_01.py
page_106_exercise_02.py
page_106_exercise_03.py
page_106_exercise_04.py
page_109_exercise_01.py
page_109_exercise_02.py
page_109_exercise_03.py
page_114_exercise_01.py
page_114_exercise_02.py
page_114_exercise_03.py
page_114_exercise_04.py
page_114_exercise_05.py
page_118_exercise_01.py
page_118_exercise_02.py
page_125_exercise_01.py
page_125_exercise_02.py
page_125_exercise_03.py
page_125_exercise_04.py


"""

import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files("."):
    print (file)