#!/usr/bin/env python3
n = int(input())
for i in range(1,n+1):
    if i % 10 == 0:
        continue
    elif i == 93:
        print('ERROR')
        break
    else:
        print(i)
