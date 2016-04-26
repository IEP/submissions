#!/usr/bin/env python3
t = 0
while True:
    try:
        t += int(input())
    except EOFError:
        break
print(t)
