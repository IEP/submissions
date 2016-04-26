#!/usr/bin/env python3
d = []
while True:
    try:
        n = int(input())
        d.append(n)
    except EOFError:
        break
d.reverse()
print('\n'.join(map(str,d)))
