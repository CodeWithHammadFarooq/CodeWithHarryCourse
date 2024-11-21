#Inheritance in Python

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print("The name of Employee : {self.id} is {self.name}")

e = Employee("Rohan Das", 400)
e.showDetails()

# Tyoes of Inheritance
'''
1. Single        Inheritance
2. Multiple      Inheritance
3. Multilevel    Inheritance
4. Hierarchical  Inheritance
5. Hybrid        Inheritance
'''