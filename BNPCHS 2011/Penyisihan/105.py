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
    cube = int(read(0))
    total = int(cube**3 - (cube-2)**3)
    print(total)
