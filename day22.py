# List in python

marks = [3, 5, 6, "Hammad", True, 8, 34, 23]
#print(marks)
#print(type(marks))
#print(marks[0])
#print(marks[1])
#print(marks[2])
#print(marks[3])
#print(marks[4])
#print(marks[5])

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3])
print(marks[2])

if 7 in marks:
    print("Yes")
else:
    print("No")

print(marks)
print(marks[1:9])
print(marks[1:9:3])

# List Comprehension:

lst = [i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)