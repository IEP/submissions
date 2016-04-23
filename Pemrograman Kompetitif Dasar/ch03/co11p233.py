#!/usr/bin/env python3
from collections import deque
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

floodCursor = [(0,-1),(-1,0),(1,0),(0,1)]
globVisit = set()

def floodFill(r,c,d):
    global M, N, globVisit
    que = deque()
    que.append((r,c))
    visited = set()
    color = d[r][c]
    print('origin',r,c)
    while len(que) > 0:
        y, x = que.popleft()
        if (y,x) not in visited:
            print(y,x)
            visited.add((y,x))
            globVisit.add((y,x))
            for (i, j) in floodCursor:
                if 0 <= y+i < M and 0 <= x+j < N:
                    if d[y+i][x+j] == color:
                        que.append((y+i,x+j))
    T = len(visited)
    return T * (T - 1)

M, N = read()
d = [read() for i in range(M)]
maks = 0
for i in range(M):
    for j in range(N):
        if (i, j) not in globVisit:
            maks = max(maks,floodFill(i,j,d)) # i = row, j = column
print(maks)
