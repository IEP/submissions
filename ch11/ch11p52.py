#!/bin/python
s, t = input().split()
s, t = str(s), str(t)
while s.find(t) != -1:
    s = s[0:s.find(t)] + s[s.find(t)+len(t):]
print(s)
