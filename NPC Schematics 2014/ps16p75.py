#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
d = read()
avg = '{:.2f}'.format(sum(d)/4)
rp = avg[:avg.index('.')]
km = avg[avg.index('.')+1:]
print('Rp {},{}'.format(rp,km))
