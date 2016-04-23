#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
b, p, l = read()

if b <= 10: bahu = 0
elif b <= 14: bahu = 1
elif b <= 18: bahu = 2
else: bahu = 3

if p <= 40: panjang = 0
elif p <= 60: panjang = 1
elif p <= 80: panjang = 2
else: panjang = 3

if l <= 90: lingkar = 0
elif l <= 120: lingkar = 1
elif l <= 180: lingkar = 2
else: lingkar = 3

ukuran = max([bahu,panjang,lingkar])
size = ('S', 'M', 'L', 'X')
print(size[ukuran])
