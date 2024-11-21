# Constructors in Python

'''There are two types of constructors
1. Parameterized construvtor
2. Default constructor'''

class Person:
    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Hammad", "Developer")
b = Person("Ammarah", "Doctor")
a.info()
b.info()
#print(a.name)