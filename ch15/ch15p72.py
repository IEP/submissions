#!/bin/python
def f(n):
    if n == 1:
        print('*')
    else:
        f(n-1)
        print('*' * n)
        f(n-1)
n = int(input())
f(n)
