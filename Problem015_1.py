"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

def routes(x, y):
    count = [[0]*(x+1) for i in range(y+1)]
    count[0][0] = 1
    for i in range(0, x+1):
        for j in range(0, y+1):
            count[i][j] += (count[i-1][j] if i-1 >= 0 else 0) + (count[i][j-1] if j-1 >= 0 else 0)
    return count[x][y]

print(routes(20, 20))
