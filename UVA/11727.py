#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
T = int(read(0))
for i in range(1,T+1):
    d = read()
    d.sort()
    print('Case {}: {}'.format(i,d[1]))
