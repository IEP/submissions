#!/usr/bin/env python3
a, b, c, d = [input() for i in range(4)]
e = a.find(b)
a = a[:e] + a[e+len(b):]
f = a.find(c)
a = a[:f+len(c)] + d + a[f+len(c):]
print(a)
