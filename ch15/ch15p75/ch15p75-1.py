#!/bin/python
import math
import sys

f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

r, c = read()
a = math.ceil(max(math.log2(r),math.log2(c)))
d = [read() for i in range(r)]
n = int(2**a)

for i in range(n):
    if i < r:
        d[i].extend([0] * (n-c))
    else:
        d.append([0] * n)

def qt(q,a,pos='',que=''):
    temp = set()
    pos += que
    for i in q:
        temp |= set(i)
    temp = list(temp)
    if len(temp) == 1:
        if temp[0] == 1:
            coord.append('1'+pos)
        return
    for i in range(2):
        for j in range(2):
            kAwal = int(j*2**(a-1))
            kAkhir = int((j+1)*2**(a-1))
            bAwal = int(i*2**(a-1))
            bAkhir = int((i+1)*2**(a-1))
            sliceQ = [q[k][kAwal:kAkhir] for k in range(bAwal,bAkhir)]
            qt(sliceQ,a-1,pos,str(i*2+j))

coord = []
qt(d,a)

print(len(coord))
if len(coord) > 0:
    print('\n'.join(coord))
