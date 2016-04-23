#!/bin/python
a = input()
n = input().split()
n = list(map(int, n))
modus = {}
for i in n:
    modus[i] = modus.get(i,0) + 1
modus = list(modus.items())
count = []
for i in range(len(modus)):
    count.append(modus[i][1])
terbesar = max(count)
for i in range(len(modus)-1,-1,-1):
    if modus[i][1] == terbesar:
        angka = modus[i][0]
        break
print(angka)
