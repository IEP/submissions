#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def prime(x):
    lim = int(x**0.5)
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2,lim+1):
        if x % i == 0:
            return False
    return True

T = int(read(0))
for i in range(T):
    N = int(read(0))
    for j in range(N,0,-1):
        if prime(j):
            print('Case #{}: {}'.format(i+1,j))
            break
