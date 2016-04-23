#!/bin/python
a = int(input())
for i in range(1,a+1):
    if i % 10 == 0:
        continue
    elif i == 42:
        print('ERROR')
        break
    else:
        print(i)
