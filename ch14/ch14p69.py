#!/bin/python
s = str(input())
palindrom = s[:] == s[::-1]
if palindrom:
    print('YA')
else:
    print('BUKAN')
