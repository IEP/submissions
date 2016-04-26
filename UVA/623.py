#!/bin/python
def f(x):
    temp = 1
    for i in range(1,x+1):
        temp *= i
    return temp

while True:
    try:
        n = int(input())
        o = str(f(n))
        print('{}!'.format(n))
        print(o)
    except EOFError:
        break
