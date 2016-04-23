#!/bin/python
n = int(input())
x = 1
for i in range(n):
    s = ''
    for j in range(n-x):
        s += ' '
    for k in range(x):
        s += '*'
    print(s)
    x += 1
