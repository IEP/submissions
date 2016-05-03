#!/usr/bin/env python3
up = down = -1
while True:
    try:
        n = int(input())
        if up == -1 and down == -1:
            up = down = n
        else:
            up = max(up,n)
            down = min(down,n)
    except EOFError:
        break
print(up-down)
