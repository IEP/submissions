#!/bin/python
import math
case = 1
while True:
    n = int(input())
    if n < 0:
        break
    ans = math.ceil(math.log2(n))
    print('Case {}: {}'.format(case,ans))
    case += 1
