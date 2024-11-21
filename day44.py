# How to import in Python

import math

result = math.sqrt(9)
print(result)

# from keyword

from math import sqrt,pi
result = sqrt(9) * pi
print(result)

# import every thing

from math import *
result = sqrt(9) * pi
print(result)

# The "as" keyword

import math as m
result = m.sqrt(9) * m.pi
print(result)

# The dir function

import math
print(dir(math))
print(math.nan, type(math.nan))