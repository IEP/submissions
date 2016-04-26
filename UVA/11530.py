#!/bin/python
press = ['adgjmptw ', 'behknqux' ,'cfilorvy', 'sz']
T = int(input())
for i in range(T):
    s = str(input())
    c = 0
    for j in s: # char read
        for k in range(4):
            if j in press[k]:
                c = c + k + 1
                break
    print('Case #{}: {}'.format(i+1,c))
