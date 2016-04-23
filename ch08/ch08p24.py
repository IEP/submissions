#!/bin/python
def agakPrima(x):
    lim = int(x**0.5)
    count = 0
    for i in range(2,lim+1):
        if x % i == 0:
            if count == 1:
                count = 0
                return False
            else:
                count += 1
    return True

for i in range(int(input())):
    if agakPrima(int(input())):
        print('YA')
    else:
        print('BUKAN')
