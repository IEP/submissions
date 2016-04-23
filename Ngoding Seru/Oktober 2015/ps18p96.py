#!/bin/python
import sys
from collections import deque
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
n = int(read(0))
d = read()
plus = list(filter(lambda x: x > 0, d))
minus = list(filter(lambda x: x < 0, d))
zero = list(filter(lambda x: x == 0, d))
non = list(filter(lambda x: x != 0, d))
if len(plus) == n:
    print(' '.join(map(str,plus)))
elif len(minus) == n:
    print(' '.join(map(str,minus)))
elif len(zero) == n:
    print(' '.join(map(str,zero)))
elif 0 <= abs(len(plus)-len(zero)) <= 1 and len(minus) == 0:
    temp = []
    if len(plus) > len(zero):
        for i in range(n):
            if i % 2 == 0:
                temp.append(plus.pop())
            else:
                temp.append(zero.pop())
    elif len(zero) > len(plus):
        for i in range(n):
            if i % 2 == 0:
                temp.append(zero.pop())
            else:
                temp.append(plus.pop())
    else:
        for i in range(n):
            if i % 2 == 0:
                temp.append(plus.pop())
            else:
                temp.append(zero.pop())
    print(' '.join(map(str,temp)))
elif 0 <= abs(len(minus)-len(zero)) <= 1 and len(plus) == 0:
    temp = []
    if len(minus) > len(zero):
        for i in range(n):
            if i % 2 == 0:
                temp.append(minus.pop())
            else:
                temp.append(zero.pop())
    elif len(zero) > len(minus):
        for i in range(n):
            if i % 2 == 0:
                temp.append(zero.pop())
            else:
                temp.append(minus.pop())
    else:
        for i in range(n):
            if i % 2 == 0:
                temp.append(minus.pop())
            else:
                temp.append(zero.pop())
    print(' '.join(map(str,temp)))
elif 0 <= abs(len(plus)-len(minus)) <= 1 and len(zero) == 0:
    temp = []
    if len(plus) > len(minus):
        for i in range(n):
            if i % 2 == 0:
                temp.append(plus.pop())
            else:
                temp.append(minus.pop())
    elif len(minus) > len(plus):
        for i in range(n):
            if i % 2 == 0:
                temp.append(minus.pop())
            else:
                temp.append(plus.pop())
    else:
        for i in range(n):
            if i % 2 == 0:
                temp.append(plus.pop())
            else:
                temp.append(minus.pop())
    print(' '.join(map(str,temp)))
elif 0 <= abs(len(non)-len(zero)) <= 1:
    temp = []
    if len(abs) > len(zero):
        for i in range(n):
            if i % 2 == 0:
                temp.append(non.pop())
            else:
                temp.append(zero.pop())
    elif len(zero) > len(abs):
        for i in range(n):
            if i % 2 == 0:
                temp.append(zero.pop())
            else:
                temp.append(non.pop())
    else:
        for i in range(n):
            if i % 2 == 0:
                temp.append(non.pop())
            else:
                temp.append(zero.pop())
    print(' '.join(map(str,temp)))
else:
    print('mustahil')
