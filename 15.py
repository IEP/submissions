#!/usr/bin/env python3
grid = [[0] * 20 for i in range(20)]
for i in range(20):
    for j in range(20):
        if i == 0 and j == 0:
            grid[i][j] = 2
        elif i != 0 and j == 0:
            grid[i][j] = grid[i-1][j] + 1
        elif i == 0 and j != 0:
            grid[i][j] = grid[i][j-1] + 1
        else:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
for i in grid:
    print(i)
