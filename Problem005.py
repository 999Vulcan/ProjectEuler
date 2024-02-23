"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#dividers = [20,19,18,17,16,15,14,13,12,11]
dividers = [2,3,4,5,6,7,8,9,10]
n = 1
while True:
    n += 1
    for divider in dividers:
        if n % divider > 0:
            break
    else:
        print(n)
        break
