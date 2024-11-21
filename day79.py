# Multiple Inheritance in Python

# syntax

'''class ChildClass(ParentClass1,ParentClass2, ParentClass3):
    class body'''


#Example

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance):
        self.dance = dance
        self.name = name

o = DancerEmployee("kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())