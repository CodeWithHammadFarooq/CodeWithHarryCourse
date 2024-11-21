# Walrus Operator in Python

a = True
print(a := False)

# use warlus operator in for loop

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())

#foods = list()
#while True:
#    food = input("What food do you like? :")
#    if food == "quit":
#        break
#    foods.append(food)

# using warlus operator

foods = list()
while (food := input("What food do you like? :")) != "quit" :
    foods.append(food)