#!/bin/python
n = int(input())
if n in range(1,10):
    print('satuan')
elif n in range(10,100):
    print('puluhan')
elif n in range(100,1000):
    print('ratusan')
elif n in range(1000,10000):
    print('ribuan')
elif n in range(10000,100000):
    print('puluhribuan')
elif n == 100000:
    print('ratusribuan')
