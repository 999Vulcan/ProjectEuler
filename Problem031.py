"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?
"""

#1
def count(amount, coins):
    c = 0
    if coins == []:
        return 1 if amount == 0 else 0
    for n in range(0, amount + 1, coins[0]):
        c += count(amount - n, coins[1:])
    return c
print(count(200, [200,100,50,20,10,5,2,1]))

#2
def count(amount, coins):
    if coins == []:
        return 0 if amount else 1
    return sum(count(amount - n, coins[1:]) for n in range(0, amount + 1, coins[0]))
print(count(200, [200,100,50,20,10,5,2,1]))

#3
def count(amount, coins):
    return sum(count(amount - n,coins[1:]) for n in range(0,amount+1,coins[0])) if coins else 0 if amount else 1
print(count(200, [200,100,50,20,10,5,2,1]))

#4 
count = lambda a, c: sum(count(a-n, c[1:]) for n in range(0, a+1, c[0])) if c else 0 if a else 1
print(count(200, [200,100,50,20,10,5,2,1]))

#5
print((lambda f:lambda a,c:f(f,a,c))(lambda f,a,c:sum(f(f,a-n,c[1:]) for n in range(0,a+1,c[0])) if c else 0 if a else 1)(200,[200,100,50,20,10,5,2,1]))

#6 (#1 with memoization)
counts = {}
values = [200,100,50,20,10,5,2,1]
def count(amount, coins):
    c = 0
    if coins == len(values):
        return 1 if amount == 0 else 0
    for n in range(0, amount + 1, values[coins]):
        if not (amount - n, coins + 1) in counts:
            counts[amount - n, coins + 1] = count(amount - n, coins + 1)
        c += counts[amount - n, coins + 1]
    return c
print(count(200, 0))
