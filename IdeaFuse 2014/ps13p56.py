#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def path(x):
    d = [x]
    x -= 1
    while x >= 1:
        x = (x-1)//2
        d.append(x+1)
    return d

T = int(read(0))
for i in range(T):
    d = read()
    a, b = path(d[0]), path(d[1])
    meet = max(list(set(a) & set(b)))
    a = a[:a.index(meet)]
    b = b[:b.index(meet)]
    result = sum(a) + sum(b) + meet
    print('Case #{}: {}'.format(i+1, result))
