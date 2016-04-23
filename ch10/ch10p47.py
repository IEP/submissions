#!/bin/python
def mapper(x):
    return list(map(int, x))

def reverser(x):
    x = str(x)
    x = x[::-1]
    x = int(x)
    return x

a = mapper(input().split())
A = reverser(a[0])
B = reverser(a[1])
print(reverser(A+B))
