#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
T = int(read(0))
for i in range(T):
    Z = int(read(0))
    N = int(read(0))
    d = []
    maks = 0;
    for j in range(N):
        temp = int(read(0))
        if j > 0:
            td = filter(lambda x: x + temp <= Z, d)
            for k in td:
                if k * temp > maks:
                    maks = k * temp
        d.append(temp)
        d.sort()
    print('Case #{}: {}'.format(i+1, maks))
