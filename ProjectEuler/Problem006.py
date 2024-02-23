"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n = 100
sum1, sum2 = 0, 0
for i in range(1, n+1):
    sum1 += i**2
    sum2 += i
diff = sum2**2 - sum1
print(diff)

#-------------

n = 100
diff = 0
for i in range(1, n):
    for j in range (i+1, n+1):
        diff += 2*i*j
print(diff)
