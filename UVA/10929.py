#!/bin/python
while True:
    n = int(input())
    if n == 0:
        break
    if n % 11 == 0:
        print('{} is a multiple of 11.'.format(n))
    else:
        print('{} is not a multiple of 11.'.format(n))

