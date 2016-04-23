#!/bin/python
import fnmatch
s = input()
N = int(input())
d = [input()[0:100] for i in range(N)]
o = []
if s != '*':
    o = [i for i in d if fnmatch.fnmatch(i, s)]
else:
    o = d
if len(o) > 0:
    print('\n'.join(o))
