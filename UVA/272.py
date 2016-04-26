#!/bin/python
counter = 0
while True:
    try:
        s = str(input())
        o = ''
        for i in range(len(s)):
            if s[i] == '"':
                if counter % 2 == 0:
                    o += '``'
                else:
                    o += '\'\''
                counter += 1
            else:
                o += s[i]
        print(o)
    except EOFError:
        break
