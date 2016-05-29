#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
for T in range(int(read(0))):
    n = int(read(0))
    print('Kang' if n % 2 == 1 else 'Kung')
