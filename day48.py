# Global variable and local variable

x = 4 # global variable
print(x)

def hello():
    x = 5 # local variable
    print(f"The local variable x is {x}")

    #print(x)
    print("Hello Hammad")
print(f"The global variable x is {x}")
hello()
x = 5
print(f"The global variable x is {x}")

# local variable plays saperate and global variable plays saperate

# local variable destroy when function is return

