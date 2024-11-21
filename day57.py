#Classes and Objects in Python

class Person:
    name       = "Hammad"
    age        =  18
    occupation = "Software Developer"
    networth   = 120000
    #self parameter      wo object jis kliye call kiya ja rha ha
    def info(self):
        print(f"{self.name} is a {self.occupation}")

#Creating Object
a = Person()
b = Person()
b.name = "Alisha"
b.occupation = "HR"
#a.name = "Ali"
#a.occupation = "Accountant"

#print(a.name, a.occupation)
a.info()
b.info()