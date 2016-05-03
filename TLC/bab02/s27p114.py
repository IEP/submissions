#!/usr/bin/env python3
from math import log
N = int(input())
if int(2**int(log(N,2))) == N:
    print('TRUE')
else:
    print('FALSE')
