#!/bin/python
def mapper(x):
    return list(map(int,x))
def jarak(a):
    global n
    return abs(a-n[1])
n = mapper(input().split())
kupon = mapper(input().split())
terkecil = (-1, -1)
for i in kupon:
    if terkecil == (-1, -1):
        terkecil = (i, jarak(i))
    elif jarak(i) < terkecil[1]:
        terkecil = (i, jarak(i))
    elif jarak(i) == terkecil[1] and i < terkecil[0]:
        terkecil = (i, jarak(i))
print(terkecil[0])
