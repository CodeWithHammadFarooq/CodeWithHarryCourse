tup = (1, 2, 3, 3, "green")
#tup[0] = 90
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
#print(tup[34])
if "green" in tup:
    print("Yes")

tup2 = tup[1:4]
print(tup2)