"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

k=5
n=10000

from math import *
from itertools import *

def sieve(n):
    s = {i for i in range(2, n+1)}
    for i in range(2, round(sqrt(n))+1):
        if i in s:
            for j in range(i*2, n+1, i):
                if j in s:
                    s -= {j}
    return s

primeset = sieve(10000000)
primelist = sorted(sieve(n)-{2})

def goodPrimes(primes):
    for twoPrimes in combinations(primes, 2):
        c1 = int(str(twoPrimes[0]) + str(twoPrimes[1]))
        c2 = int(str(twoPrimes[1]) + str(twoPrimes[0]))
        if not (c1 in primeset and c2 in primeset):
            return False
    return True

def generateSubsets(subset, s):
    primes = [primelist[i] for i in subset]
    #print(subset, sum(primes))
    if len(primes) == k and sum(primes) == s:
        yield subset
    if len(primes) < k and sum(primes) < s:
        start = subset[-1]+1 if subset else 0
        for i in range(start, len(primelist)):
            if sum(primelist[i] for i in subset+[i]) > s:
                break
            for ss in generateSubsets(subset+[i], s):
                yield ss

minsum = 1
while True:
    minsum += 1
    print(minsum)
    for subset in generateSubsets([], minsum):
        if goodPrimes(primelist[i] for i in subset):
            print("*"*10, minsum)
            minsum = 0
            break
    if not minsum:
        break

"""
for primes in combinations(primelist, k):
    if sum(primes) > minsum:
        continue
    if goodPrimes(primes):
        minsum = min(minsum, sum(primes))
        print(primes, minsum)
    
print(minsum)
"""
