# Single Inheritance in Python

'''It is the most common type of inheritance'''

# syntax is

#class ChildClass(ParentClass):
    #class body

# Example:

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")