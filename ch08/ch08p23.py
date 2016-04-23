#!/bin/python
def prime(x):
    limit = int(x**0.5)
    for i in range(2,limit+1):
        if x % i == 0:
            return False
    return True

for i in range(int(input())):
    if prime(int(input())):
        print('YA')
    else:
        print('BUKAN')
