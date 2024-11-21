# Map, Filter and Reduce in Python


# Map()
def cube(x):
    return x*x*x
print(cube(2))
l = [1,2,4,6,4,3]
#newl = []
#for item in l:
#    newl.append(cube(item))

# lamda

#newl = list(map(lamda x: x*x*x, l))
newl = list(map(cube, l))
print(newl)

# filter()

def filter_function(a):
    return a>2

newnewl = list(filter(filter_function, l))
print(newnewl)

# reduce()


from functools import reduce
numbers = [1,2,3,4,5]
def mysum(x, y):
    return x + y
sum = reduce(mysum, numbers)
print(sum)