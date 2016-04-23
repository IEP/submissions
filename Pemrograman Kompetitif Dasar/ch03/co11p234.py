#!/usr/bin/env python3
from collections import deque
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

floodCursor = [(0,-1),(-1,0),(1,0),(0,1)]
globVisit = set()
score = {}

def floodFill(r,c,d):
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
    return T * (T - 1), list(visited)

def runtuh(d):
    limit = []
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
            temp = floodFill(i,j,d)
            if temp[0] > maks:
                maks = temp[0]
                region = temp[1]
for i, j in region:
    d[i][j] = '.'
d = [list(map(str,i)) for i in d]
runtuh(d)
print('\n'.join(' '.join(i) for i in d))
