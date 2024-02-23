from math import *
from functools import *
print(reduce(lambda a, b: int(a) + int(b), str(factorial(100))))
