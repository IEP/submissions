#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(str,inp.split()))
while True:
    try:
        s = read()
        print(' '.join(map(lambda x: x[::-1],s)))
    except EOFError:
        break
