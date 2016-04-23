#!/usr/bin/env python3
from collections import deque
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

floodCursor = [(0,-1),(-1,0),(1,0),(0,1)]
globVisit = set()
area = []

def floodFill(r,c,d,mode=1):
    visited = set()
    q = deque()
    q.append((r,c))
    color = d[r][c]
    while len(q) > 0:
        y, x = q.popleft()
        if (y,x) not in visited:
            visited.add((y,x))
            globVisit.add((y,x))
            for i, j in floodCursor:
                if 0 <= y+i < M and 0 <= x+j < N:
                    if d[y+i][x+j] == color:
                        q.append((y+i,x+j))
    T = len(visited)
    if mode == 1:
        area.append((list(visited), T * (T-1)))
    if color == '.':
        return 0, list(visited)
    else:
        return T * (T - 1), list(visited)

def runtuh(d,colorize):
    limit = []
    for i, j in colorize:
        d[i][j] = '.'
    for j in range(N):
        for i in range(M-1,-1,-1):
            if d[i][j] == '.':
                limit.append((i,j))
                break
    for i, j in limit:
        temp = [d[k][j] for k in range(i+1)]
        temp1 = deque()
        for k in temp:
            if k == '.':
                temp1.appendleft(k)
            else:
                temp1.append(k)
        for k in range(i+1):
            d[k][j] = temp1[k]

M, N = read()
d = [read() for i in range(M)]
maks = 0
for i in range(M):
    for j in range(N):
        if (i,j) not in globVisit:
            floodFill(i,j,d)

d = [list(map(str,i)) for i in d]
maks = 0
for region, score in area:
    globVisit = set()
    e = [i[:] for i in d]
    runtuh(e, region)
    for i in range(M):
        for j in range(N):
            if (i, j) not in globVisit:
                maks = max(maks, floodFill(i,j,e,2)[0] + score)
print(maks)
