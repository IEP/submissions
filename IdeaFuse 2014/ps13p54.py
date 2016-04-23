#!/bin/python
import sys
import math
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
T = int(read(0))
for i in range(T):
    O = read()
    N = int(read(0))
    d = [read() for j in range(N)]
    star = 0
    angle = []
    for j in d:
        Dx = j[0] - O[0]
        Dy = j[1] - O[1]
        temp = math.atan2(Dy, Dx)
        if temp not in angle:
            angle.append(temp)
            star += 1
    print('Case #{}: {}'.format(i+1, star))
