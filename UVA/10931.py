#!/bin/python
while True:
    n = int(input())
    if n == 0:
        break
    b = str(bin(n))[2:]
    temp = list(b)
    temp = map(int,temp)
    p = sum(temp)
    print('The parity of {} is {} (mod 2).'.format(b,p))
