#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
tc = int(read(0))
for i in range(tc):
    n, m = read()
    d = [read() for j in range(m)]
    vote = [0] * n
    for j in range(n):
        for k in range(m):
            vote[j] += d[k][j]
    highest = max(vote)
    print(vote.index(highest)+1)
