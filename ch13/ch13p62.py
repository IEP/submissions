#!/bin/python
s = []
for i in range(int(input())):
    temp = str(input())
    s.append(temp)
    s.sort()
    print(s.index(temp)+1)
