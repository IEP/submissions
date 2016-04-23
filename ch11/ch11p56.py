#!/bin/python
s = str(input())
changed = []
o = ''
snake = 2
for i in range(len(s)):
    if s[i] == '_':
        snake = 1
    elif s[i].isupper():
        snake = 0
    changed.append(False)
if snake == 1:
    for i in range(len(s)):
        if s[i] == '_':
            o += s[i+1].upper()
            changed[i] = True
            changed[i+1] = True
        if not(changed[i]):
            o += s[i]
            changed[i] = True
elif snake == 0:
    for i in range(len(s)):
        if s[i].isupper():
            o += '_'
            o += s[i].lower()
        else:
            o += s[i]
elif snake == 2:
    for i in range(len(s)):
        o += s[i]
print(o)
