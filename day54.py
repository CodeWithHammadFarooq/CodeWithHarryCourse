# 'is' vs '==' in Python


a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
#a = 4
#b = "4"
#a = 4
#b = 4

print(a is b)  # exact location of object in memory
print(a == b)   # value