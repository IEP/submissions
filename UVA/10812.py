#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
for i in range(int(read(0))):
    x, y = read()
    a = (x + y)//2
    b = (x - y)//2
    if a < 0 or b < 0 or a+b != x:
        print('impossible')
    else:
        print("{} {}".format(a,b))
