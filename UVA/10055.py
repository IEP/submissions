#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
while True:
    try:
        d = read()
        print(abs(d[0]-d[1]))
    except EOFError:
        break
