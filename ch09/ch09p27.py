#!/bin/python
def mapper(x):
    return list(map(int, x))
a = input().split()
a = mapper(a)
panjang = a[0]*a[1]
b = []
for i in range(1,a[0]+1):
    c = input().split()
    c = mapper(c)
    b.append(c)

for i in range(a[1]):
    o = ''
    for j in range(a[0]-1,-1,-1):
        o += str(b[j][i])
        if j > 0:
            o += ' '
    print(o)
