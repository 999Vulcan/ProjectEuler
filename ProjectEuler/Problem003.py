"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
factor = 1
while number > 1:
    factor += 1
    while number % factor == 0:
        number //= factor
print(factor)
