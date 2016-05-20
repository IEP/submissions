#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
o = ['salah', 'mungkin', 'benar']
c = {'B': 2, 'S': 0, '~B': 0, '~S': 2}
for T in range(int(read(0))):
    m = read(0)
    res = 2
    for i in m.split('^'):
        if res == 0: break
        res = min(res,c.get(i,1))
    print(o[res])
