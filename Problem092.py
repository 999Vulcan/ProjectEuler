"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

memo = {1:1,89:89}
maxnum = 10**7
n = 0

def sumSquares(num):
    sumsquares = 0
    for digit in str(num):
        sumsquares += int(digit)**2
    return sumsquares

def chain(num):
    if num in memo:
        return(memo[num])
    else:
        sumsquares = sumSquares(num)
        c = chain(sumsquares)
        memo[num] = c
        return c

for num in range(2, maxnum):
    c = chain(num)
    if c == 89: n += 1

print(n)
    
