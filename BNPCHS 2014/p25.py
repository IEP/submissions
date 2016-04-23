#!/bin/python
import sys

f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = f.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

n = int(read(0))
for i in range(n):
    read(0) # dummy
    d = [read() for j in range(2)]
    smallest = -1
    for j in d[0]:
        for k in d[1]:
            if smallest == -1:
                smallest = abs(k-j)
            elif abs(k-j) < smallest:
                smallest = abs(k-j)
    print('Kasus #{}: {}'.format(i+1,smallest))
