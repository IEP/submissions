#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
a, b = read()
print('masing-masing {}'.format(a//b))
print('bersisa {}'.format(a%b))
