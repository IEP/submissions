#!/bin/python
while True:
    try:
        a = str(input())
    except EOFError:
        break
    print (a)
