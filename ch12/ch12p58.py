#!/bin/python
def m(x):
    return list(map(int,x))
def ce(y,x):
    global a
    global c
    if x == -1 or x == a[1] or y == -1 or y == a[0]:
        return 1
    return c[y][x]
a = m(input().split()) # 0: y, 1: x, 2: k
c = []                 # y = baris, x = kolom
o = (0,0)
for i in range(a[0]): # input baris based
    c.append(m(input().split()))
for j in range(a[1]): # loop utama kolom
    if o != (0,0): break # cek
    for i in range(a[0]): # loop sekunder baris
        if o != (0,0): break # cek
        # atas, bawah, kiri, kanan
        ans = ce(i-1,j)*ce(i+1,j)*ce(i,j-1)*ce(i,j+1)
        if ans == a[2]: # cek kemenarikan
            o = (i+1,j+1)
print('{} {}'.format(o[0],o[1]))
