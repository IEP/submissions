#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
N, M = read()
d = [read() for i in range(N)]
d = [i[::-1] for i in list(zip(*d))]
for i in d:
    print(' '.join(map(str,i)))
