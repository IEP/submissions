#!/usr/bin/env python3
n = int(input())
c = 0
for i in range(1,n+1):
    temp = ''
    for j in range(1,i+1):
        temp += str(c)
        c += 1
        if c >= 10:
            c = 0
    print(temp)
