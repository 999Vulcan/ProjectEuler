from math import *

"""
n = int(3000)
k = 1.1

while 2*k*(k-1) != n*(n-1):
    n += 1
    a = n*(n-1)
    k = round((sqrt(2*a+1)+1)/2)
print(k, n)
"""

n = 1e12
a = n*(n-1)
k = round((sqrt(2*a+1)+1)/2)

while 2*k*(k-1) != n*(n-1):
    k += 1
    a = 2*k*(k-1)
    n = round((sqrt(4*a+1)+1)/2)
    if k%1e7 == 0: print(k, n)

print(k, n)
