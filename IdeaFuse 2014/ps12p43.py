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
    a, b = read()
    low = min(a,b)
    high = max(a,b)
    while True:
        if low == high:
            o = low
            break
        elif low > high:
            o = 'impossible'
            break
        else:
            low += 7
            high -= 5
    print('Case #{}: {}'.format(i+1,o))
