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
    s = str(read(0))
    if len(s) == 1:
        if s == 'B':
            print('benar')
        elif s == 'S':
            print('salah')
        else:
            print('mungkin')
    else:
        c = []
        for j in s:
            if j == '~': c.append('not')
            elif j == '^': c.append('and')
            elif j == 'B': c.append(1)
            elif j == 'S': c.append(0)
        aCur = 0

