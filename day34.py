# Dictionary methods in python

# 1. update()

ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

ep1.update(ep2)
print(ep1)

# 2.Clear()

ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

ep1.clear()
print(ep1)
empt = {}
print(empt)

# 3. POP()

ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

ep1.pop(122)
print(ep1)

# 4. POPitem()    it use for remove last key pir value in dictionary

ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

ep1.popitem()
print(ep1)

# 4. del:

ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

#del ep1
del ep1[122]
print(ep1)



