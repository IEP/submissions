#!/bin/python
n = int(input())
x = 0
for i in range(1,n+1):
    s = ''
    for j in range(i):
        s += str(x)
        x += 1
        if (x == 10):
            x = 0
    print(s)
