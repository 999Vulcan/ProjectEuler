"""
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

print(sum(n if sum(int(d)**5 for d in str(n)) == n else 0 for n in range(10,999999)))

