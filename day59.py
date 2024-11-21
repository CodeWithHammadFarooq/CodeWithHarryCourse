#Decorators in Python

def great(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanx for using this function")
        return mfx

@great
def hello():
    print("Hello world")

def add (a, b):
    print(a+b)

#great(hello)()
#hello()