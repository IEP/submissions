#!/bin/python
T = int(input())
for i in range(T):
    n = int(input())
    n = n * 567
    n = n // 9
    n = n + 7492
    n = n * 235
    n = n // 47
    n = n - 498
    n = str(n)
    print(n[-2])
