# Generators in Python

def my_generator():
    for i in range(7999):
        #complex computations
        yield i

gen = my_generator()
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

for j in gen:
    print(j)