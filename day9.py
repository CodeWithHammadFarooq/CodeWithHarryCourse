#Explicit Conversion or Explicite typecastint:
    #Which do by us
    #For example
a = "2"
b = "3"
print(int(a)+int(b))
#and other example is:
string = "15"
number = 7
string_number = int(string)   #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is : ", sum)
#Ixplicit Conversion or Ixplicite typecastint:
    #Which do by python
    #For example


#Python automatically converts
#a to int
a = 7
print(type(a))
#Python automatically converts b to float
b = 3.0
print(type(b))
#Python automatically converts c to float as itis a float addition
c = a+b
print(type(c))

