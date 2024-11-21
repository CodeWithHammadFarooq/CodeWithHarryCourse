# DFunction Arguments in python
def average(a=9, b=1):
    print("The average is", (a+b)/2)
    #average(4, 6)
average(1,5)

#Default argument:

def average(a=9, b=1):
    print("The average is", (a+b)/2)
    #average(4, 6)
average(b=9)

#for example

def name(fname, mname = "Hammad", lname = "Haseeb"):
    print("Hello,", fname, mname, lname)
name("Zayn", "Yasir", "Salman")

#Keyword Arguments:

def average(a, b, c=1):
    print("The average is", (a+b+c)/2)
#average(b=9)
average(5,6)

#Variable-lenght argument:

def average(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is :", sum / len(numbers))
average(5, 6, 7, 1)

#Return Statement:

def average(*numbers):

    sum = 0
    for i in numbers:
        sum = sum + i
        return 7

        #return sum / len(numbers)
        #print("Average is :", sum / len(numbers))
c = average(5, 6, 7, 1)
print(c)
