#!/usr/bin/env python3
import math
for T in range(1, int(input()) + 1):
    N = int(input())
    d = [int(input()) for i in range(N)]
    dataSize = math.ceil(sum(d)/1000)
    space = int(2 ** math.ceil(math.log(dataSize, 2)))
    print('Case #{}: {}GB'.format(T, max(16, space)))