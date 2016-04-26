#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
x1, y1, x2, y2 = read()
print(abs(x1-x2) + abs(y1-y2))
