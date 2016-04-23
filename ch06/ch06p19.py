#!/bin/python
a, b = input().split()
a = int(a)
b = int(b)
s = ''
for i in range(1,a+1):
    if i % b == 0:
        s += '*'
    else:
        s += str(i)
    if i < a:
        s += ' '
print(s)
