#!/bin/python
N = int(input())
if N >= 10000:
    print('puluhribuan')
elif N >= 1000:
    print('ribuan')
elif N >= 100:
    print('ratusan')
elif N >= 10:
    print('puluhan')
else:
    print('satuan')
