"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

"""
def isPower(n):
    return round(n ** (1/len(str(n))), 14) % 1 == 0
count = 0
for i in range(10**10):
    if isPower(i):
        count += 1
        print(count, i)

print(count)
"""

count = 0
for i in range(1,25):
    for j in range(1,25):
        if len(str(i**j)) == j:
            count += 1
            print(count, i**j)
print(count)
