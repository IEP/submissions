#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
Te = int(read(0))
for i in range(Te):
    n = int(read(0))
    d = read()
    counter = {}
    for j in d:
        counter[j] = counter.get(j,0) + 1
    counter = list(counter)
    print(counter)
