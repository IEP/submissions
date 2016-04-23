#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
a, b, c = read()
d, e, f = read()
g, h, i = read()
print('{} {} {}'.format(a,d,g))
print('{} {} {}'.format(b,e,h))
print('{} {} {}'.format(c,f,i))
