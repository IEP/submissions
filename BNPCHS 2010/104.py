#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
n = int(read(0))
for i in range(n):
    n, m = read()
    gaji = read()
    gaji.sort(reverse=True)
    if sum(gaji) <= m:
        print(-1)
        continue
    else:
        while min(gaji) < m//len(gaji):
            m -= gaji.pop()
        print(m//len(gaji))
