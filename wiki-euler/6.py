#!/usr/bin/env python3
a = sum([i for i in range(1,101)])**2
b = sum([i**2 for i in range(1,101)])
print(int(a-b))
