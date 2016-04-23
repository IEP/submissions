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
    d = read(1)
    d[0:4] = list(map(int,d[0:4]))
    d[4] = str(d[4])
    gain = d[3] - d[0] * d[1] * d[2]
    if d[4] == 'bayar':
        print(gain)
    elif d[4] == 'kabur':
        print(gain-d[3])
