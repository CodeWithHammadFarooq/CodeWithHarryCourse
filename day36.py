# Exception Handling in Python
a = input("Enter number of table : ")
print(f"Multiplication table of {a} is : ")
try:
    for i in range(1, 11):
        print(f"{int (a)} x {i} = {int(a)*i}")

except Exception as e:
    print("Sorry some error occured")

print("Some important lines of code")
print("End of program")

try:
    num = int(input("Enter an integer : "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")

except IndexError:
    print("Index Error")