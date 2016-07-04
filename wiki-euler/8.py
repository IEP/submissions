#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
temp = ''.join([read(0) for i in range(20)])
res = 0
for i in range(1000-13):
    d = temp[i:i+13]
    temp1 = 1
    for j in d:
        temp1 *= int(j)
    res = max(res,temp1)
print(res)
