# Access Modifiers in Python

'''Types of access specifiers
1. Public access modifiers
2. Private access modifiers
3. Protected access modifiers
'''
# Public Access Specifiers Modifer

class Employee:
    def __init__(self):
        self.name = "Hammad"

a = Employee()
print(a.name)

# In Private Access Specifiers Modifer

#print(a.__name)   cannot be access directly but indirectly
#print(a._Employee__name)
print(a.__dir__())

# In Protected Access Specifiers Modifer

class Student:
    def __init__(self):
        self._name = "Hammad"

    def _funName(self):       #protected method
        return "Guiding Light"

    class Sbject(Student):      #inherited class
        pass

obj = Student()
obj1 = Subject()

# calling by object of student class
print(obj._name)
print(obj1._funName())
# calling by object of subject class
print(obj._name)
print(obj1._funName())