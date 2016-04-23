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
    n = int(read(0))
    temp = read()
    pos = list(filter(lambda x: x >  0, temp))
    neg = list(filter(lambda x: x <  0, temp))
    zer = list(filter(lambda x: x == 0, temp))
    non = list(filter(lambda x: x != 0, temp))
    d = [pos,neg,zer,non]
    t = [len(pos),len(neg),len(zer),len(non)]
    if max(t[0:3]) == n:
        cur = d[t.index(n)]
        print(' '.join(map(str,cur)))
