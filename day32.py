# Sets method in Python

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))

s1.update(s2)
print(s1, s2)


s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.intersection(s2))

s1.intersection_update(s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)

# Sets Method

# isdisjoint():

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities2 = {"Tokyo", "Soul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset():

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities2 = {"Soul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Soul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))

# issubset():

cities3 = {"Soul", "Madrid", "Kabul"}
print(cities.issubset(cities3))

# add():

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities.add("Helsinki")
print(cities)

# update()

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities2 = {"Soul", "Kabul"}
cities.update(cities2)
print(cities)

# remove()/discard()

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities.discard("Tokyo2")
print(cities)

# pop()

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
item = cities.pop()
print(cities)
print(item)

# del            is a keyword

#cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
#del cities
#print(cities)

# clear()

cities = {"Tokyo", "Madrid", "Berlin", "Dehli"}
cities.clear()
print(cities)
