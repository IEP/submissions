#!/bin/python
s = str(input())
o = ''
for i in s:
    if i.isupper():
        o += i.lower()
    elif i.islower():
        o += i.upper()
print(o)
