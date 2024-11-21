a = int(input("Enter Your age : "))
print("Your age is, a")

#Conditional Operator
#  == , != , < , > , <= , =>

#print(a<18)
#print(a>18)
#print(a==18)
#print(a!=18)
#print(a<=18)
#print(a>=18)
if (a<18):
    print("You cannot drive")
else:
    print("You can drive")

# If-else statement

applePrice = 210
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 Kg Apples to the cart.")
elif(budget - applePrice > 70):
    print("Its okay you can buy")
else:
    print("Alexa, do not add to the cart")

#elif
num = int(input("Enter the value of num :"))
if (num < 0):
    print("Number is Negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is Positive.")
print("I am happy now.")

#Nested-if-else
num = 18
if (num < 0):
    print("Number is Negative.")
elif (num > 0):
   if (num <= 10):
        print("Number is between 1-10")
   elif (num > 10 and num <= 20):
        print("Number between 11-20")
   else:
        print("Number is greater than 20")
else:
    print("Number is Zero.")