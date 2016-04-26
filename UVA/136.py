#!/bin/python
ugly = [False] * 1000000
for i in range(1,7):
    ugly[i] = True
for i in [2,3,5]:
    for j in range(i,1000000,i):
        ugly[j] = True
o = []
for i in range(1000000):
    if len(o) == 1500:
        break
    if ugly[i] == True:
        o.append(i)
print(o[1499])
