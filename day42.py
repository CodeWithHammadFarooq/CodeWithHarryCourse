# Enumerate Function in Python

marks = [45, 78, 56, 46, 68, 98, 75]
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 5):
        print("Hammad, awesome!")

