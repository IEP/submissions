#!/bin/python
a = int(input())
i = input().split()
i = list(map(int, i))
print('{} {}'.format(max(i), min(i)))
