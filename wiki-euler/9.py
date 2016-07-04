#!/usr/bin/env python3
import math
def triplet():
    for c in range(999,0,-1):
        for b in range(c-1,0,-1):
            a = math.floor(math.sqrt(c**2 - b**2))
            if a + b + c == 1000 and \
            int(a**2) + int(b**2) == int(c**2):
                print(a,b,c)
                return a, b, c
a, b, c = triplet()
print(a*b*c)
