#!/bin/python
s = []
while True:
    try:
        s.append(str(input()))
    except EOFError:
        break
for i in range(len(s)-1,-1,-1):
    print(s[i])
