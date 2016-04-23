#!/bin/python
import sys
import math
import itertools

f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def qtTrans(que,a):
    global d
    for i in que:
        z = a
        i = i[1:]
        regionBaris = [j for j in range(z)]
        regionKolom = [k for k in range(z)]
        for j in i:
            baris = (0,z//2) if int(j) < 2 else (z//2,z)
            kolom = (0,z//2) if int(j) % 2 == 0 else (z//2,z)
            regionBaris = regionBaris[baris[0]:baris[1]]
            regionKolom = regionKolom[kolom[0]:kolom[1]]
            z = z//2
        block = itertools.product(regionBaris,regionKolom)
        for j in block:
            d[j[0]][j[1]] = 1

n = int(read(0))
q = [str(read(0)) for i in range(n)]
r, c = read()
p = math.ceil(max(math.log2(r),math.log2(c)))
a = int(2**p)
d = [[0] * a for i in range(a)]

qtTrans(q,a)

for i in range(r):
    print(' '.join(map(str,d[i][:c])))
