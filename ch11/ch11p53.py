#!/bin/python
def caesar(c,k):
    c = ord(c) + k
    if c > ord('z'):
        c -= 26
    return chr(c)
s = str(input())
k = int(input())
o = ''
for i in s:
    o += caesar(i,k)
print(o)
