#!/bin/python
def m(x):
    return list(map(int,x))
d = {}
a = m(input().split())
for i in range(a[0]):
    b = input().split()
    d[str(b[0][:10]).lower()] = str(b[1][:6])
for j in range(a[1]):
    b = str(input())
    print(d.get(b[:10].lower(),'NIHIL'))
