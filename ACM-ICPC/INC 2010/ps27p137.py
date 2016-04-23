#!/bin/python
import sys
from collections import deque
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
T = int(read(0))
for i in range(T):
    s = str(read(0))
    d = deque()
    cur = 0 # 0 back 1 front
    for j in range(len(s)):
        if s[j] == '+':
            if cur == 0:
                d.append(s[j+1])
            else:
                d.appendleft(s[j+1])
        elif s[j] == '^':
            if cur == 0:
                cur = 1
            else:
                cur = 0
    d = list(d)
    if cur == 1:
        d.reverse()
    print(''.join(d))
