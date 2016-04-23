#!/bin/python
total = 0
while True:
    try:
        i = int(input())
        total += i
    except EOFError:
        break
print (total)

