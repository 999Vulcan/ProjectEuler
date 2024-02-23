"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""

triangle = []
for line in open("Problem067.txt"):
    triangle.append([int(word) for word in line.split()])
n = len(triangle)
for i in range(n-2, -1, -1):
    for j in range(i+1):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
print(triangle[0][0])
