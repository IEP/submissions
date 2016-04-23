#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
def check(a):
    if len(a[0]) != 5 or (not 0 <= a[1] <= 500) or (not 0 <= a[2] <= 1000) or (not 0 <= a[3] <= 500):
        return False
    for i in a[0]:
        if not(i.isupper() or i.isdigit()):
            return False
    return True
T = int(read(0))
for i in range(T):
    N, M = read()
    case = read(0)
    data = []
    for j in range(N):
        temp = read(1)
        temp[1:4] = map(int,temp[1:4])
        if check(temp):
            data.append(temp)
    data.sort(key=lambda x: (x[3], x[2], x[1]), reverse=True)
    print('YA' if case in [j[0] for j in data[0:M]] else 'TIDAK')
