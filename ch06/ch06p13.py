#!/bin/python
a = int(input())
b = input().split()
c = 0
for i in range(a):
    b[i] = int(b[i])
    c += b[i]
print(c)
