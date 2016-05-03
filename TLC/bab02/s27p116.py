#!/usr/bin/env python3
d = [float(input()) for i in range(int(input()))]
print('{:.2f} {:.2f} {:.2f}'.format(min(d),max(d),sum(d)/len(d)))
