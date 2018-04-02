#!/usr/bin/env python

dictionary = {'normal': 100,
              'fighting': 200,
              'flying': 300,
              'poison': 400,
              'ground': 500,
              'rock': 600,
              'bug': 700,
              'ghost': 800,
              'steel': 900,
              'fire': 1000,
              'water': 1100,
              'grass': 1200,
              'electric': 1300,
              'psychic': 1400,
              'ice': 1500,
              'dragon': 1600,
              'dark': 1700,
              'fairy': 1800,
              'legend': 10000}

ballType = {1: 'poke ball',
            2: 'great ball',
            3: 'ultra ball',
            100: 'masterball'}

result = 0

for _ in range(int(input())):
    pokemonType, strength = input().split()
    strength = int(strength)
    if strength <= 1000:
        ball = 1
    elif strength <= 2000:
        ball = 2
    elif strength <= 3000:
        ball = 3
    else:
        ball = 100
    typeMultiplier = dictionary[pokemonType.lower()]
    result += typeMultiplier * ball
    print('{} {}'.format(pokemonType.capitalize(), ballType[ball]))
print('{}'.format(result))