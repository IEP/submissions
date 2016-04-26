#!/bin/python
lang = {'HELLO': 'ENGLISH',
        'HOLA': 'SPANISH',
        'HALLO': 'GERMAN',
        'BONJOUR': 'FRENCH',
        'CIAO': 'ITALIAN',
        'ZDRAVSTVUJTE': 'RUSSIAN'}
c = 1
while True:
    s = str(input())
    if s == '#':
        break
    o = lang.get(s,'UNKNOWN')
    print('Case {}: {}'.format(c,o))
    c += 1
