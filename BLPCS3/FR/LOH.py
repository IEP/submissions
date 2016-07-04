#!/usr/bin/env python3
s = input()
mantra = []
for T in range(int(input())):
    mantra.append(input())
spell = ''
for i in s:
    spell += i
    for j in mantra:
        if len(spell) >= len(j):
            if spell[-len(j):] == j:
                spell = spell[0:-len(j)]
print(spell)
