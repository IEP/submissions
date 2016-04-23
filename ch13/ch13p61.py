#!/bin/python
n = int(input())
s = []
pendek = -1
panjang = -1
o = []
for i in range(n):
    temp = str(input())
    if pendek == -1 and panjang == -1:
        pendek = len(temp)
        panjang = len(temp)
    elif len(temp) < pendek:
        pendek = len(temp)
    elif len(temp) > panjang:
        panjang = len(temp)
    s.append(temp)
s.sort()
#print(s)
for i in range(pendek,panjang+1):
    for j in range(len(s)):
        if i == len(s[j]):
            o.append(s[j])
for i in o:
    print(i)
