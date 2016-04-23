#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def fibgen(x=93):
    a, b = 1, 1
    for i in range(x):
        yield a
        a, b = b, a+b

fib = list(fibgen())

n = int(read(0))
for i in range(n):
    read(0) # dummy
    d = read()
    t = 0
    for j in d:
        t += fib[j]
    print('Case #{}: {}'.format(i+1, t))
