#!/usr/bin/env python3
for T in range(int(input())):
    s = input()
    if len(s) > 10:
        s = s[0] + str(len(s)-2) + s[-1]
    print(s)
