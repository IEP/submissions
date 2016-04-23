#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
a, b = list(map(str,read(1)))
t = 0
for i in a:
    for j in b:
        ta = int(i)
        tb = int(j)
        t += ta * tb
print(t)
