#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
while True:
    n = int(read(0))
    if n == 0: break
    d = [read() for i in range(n)]
    row = []
    col = []
    for i in range(n):
        if sum(d[i]) % 2 != 0:
            row.append(i+1)
    for i in range(n):
        total = 0
        for j in range(n):
            total += d[j][i]
        if total % 2 != 0:
            col.append(i+1)
    if len(row) == 0 and len(col) == 0:
        print('OK')
    elif len(row) == 1 and len(col) == 1:
        print('Change bit ({},{})'.format(row[0],col[0]))
    else:
        print('Corrupt')
