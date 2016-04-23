#!/bin/python
i = int(input())
for j in range(i-1,0,-1):
    if i % j == 0:
        print (j)
