# Python Dictionaries

dict = {
        "Hammad" : "Human being",
        "Spoon " : "Object"
        }
print(dict["Hammad"])
info = {'name': 'Karan', 'age' : 19, 'eligible' : True}
print(info['name'])
print(info.get('name'))
print(info.keys())
print(info.values())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
     print(f"The value corresponding to the key {key} is (value)")

