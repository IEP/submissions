#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
N, K = read()
d = read()
neg = list(filter(lambda x : x < 0, d))
pos = list(filter(lambda x: x >= 0, d))
flip = min(K, len(neg))
for i in range(flip):
    neg[i] = neg[i] * -1
print(sum(neg)+sum(pos))
print('{} {}'.format(0, N-1))
