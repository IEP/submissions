#!/usr/bin/env python3
for T in range(1, int(input()) + 1):
    N = int(input())
    countMap = {4: 0, 5: 0, 6: 0}
    for i in range(N):
        temp = input()
        countMap[len(temp)] = countMap.get(len(temp), 0) + 1
    print('Case #{}: {} {} {}'.format(T, countMap[4], countMap[5], countMap[6]))