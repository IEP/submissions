#!/bin/python
import sys
from collections import deque
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def legal(y,x):
    global m, n, d
    if y == -1 or x == -1 or y == m or x == n:
        return False
    return d[y][x]

def flood():
    global m, n, d, cur
    q = deque([cur])
    color = d[cur[0]][cur[1]]
    v = []
    move = []
    while len(q) > 0:
        y, x = q.popleft()
        if [y,x] in move:
            continue
        if d[y][x] == color:
            move.append([y,x])
            v.append([y,x])
        else:
            move.append([y,x])
        if legal(y-1,x) == color:
            q.append([y-1,x])
        if legal(y,x+1) == color:
            q.append([y,x+1])
        if legal(y+1,x) == color:
            q.append([y+1,x])
        if legal(y,x-1) == color:
            q.append([y,x-1])
    return len(v)

m, n = read()
d = [read() for i in range(m)]
cur = read()

score = flood()
print(score*(score-1))
