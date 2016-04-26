#!/usr/bin/env python3
while True:
    try:
        s = input()
        print(s)
    except EOFError:
        break
