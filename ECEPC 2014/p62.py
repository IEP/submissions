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
    N, L = read()
    d = []
    for j in range(N):
        dob, nama = read(1)
        dob = str(dob)
        dob = dob.split('/')
        dob = dob[2] + dob[0] + dob[1]
        nama = str(nama)
        d.append([int(dob),nama])
    d.sort(key=lambda x: x[0])
    print('Case #{}: {}'.format(i+1,d[L-1][1]))
