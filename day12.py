#slicing of a string

names = "Hammad, Ammar"
#print(names[0:6])

len1 = len(names)
print("Hammad is a", len1,"letter word")

#String as an array

fruit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])#including 0 but not 4
print(fruit[:4])#including 1 but not 4
print(fruit[0:-4])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[-1:-3])
print(fruit[-3:len(fruit)-1])

#Quick Quiz:

nm = "harry"
print(nm[-4:-2])

#Loop through a string

alphabets = "ABCDE"
for i in alphabets:
    print(i)
