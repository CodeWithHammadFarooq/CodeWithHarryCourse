# Menuplating Tuple

#countries = ("Spain","Italy", "India","England", "Germany")
#temp = list(countries)
#temp.append("Russia")   # add item
#temp.pop(3)             # remove item
#temp[2] = "Finland"     # change item
#countries = tuple(temp)
#print(countries)

#countries = ("Pakistan", "Afghanistan", "Bangladesh", "Srilanka")
#countries2 = ("Vietnam", "India", "China")
#southEastAsia = countries + countries2
#print(southEastAsia)

# Tuples methods in python

tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 3)
#res = tuple1.count(3)
#res = tuple1.index(3)
res = tuple1.count(3)
res = len(tuple1)
print('Count of 3 in Tuple1 is : ', res)