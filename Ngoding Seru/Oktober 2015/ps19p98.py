#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
T = int(read(0))
for i in range(T):
    x = int(read(0))
    s = str(read(0))
    d = {}
    cur = 0
    for j in s:
        if j == '[':
            cur += 1
            for k in range(cur):
                d[k+1] = d.get(k+1,'') + j
        elif j == ']':
            for k in range(cur):
                d[k+1] = d.get(k+1,'') + j
            cur -= 1
        else:
            for k in range(cur):
                d[k+1] = d.get(k+1,'') + j
    temp = ''
    cur = 0
    ans = d[x]
    o = []
    for j in ans:
        if j == '[':
            cur += 1
        elif j == ']':
            cur -= 1
        temp += j
        if cur == 0:
            o.append(temp)
            temp = ''
    print(len(o))
    print('\n'.join(o))
