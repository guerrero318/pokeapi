#!/usr/bin/python3
import requests
import string
from pokeascii import ascii
import sys
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def main():
    NAME_URL = f'https://pokeapi.co/api/v2/pokemon/?limit=151'
    names = requests.get(NAME_URL).json()['results']

    pokemon_list = []
    for poke in names:
        pokemon_list.append(poke['name'])

    name = ''
    while name == "" or name not in pokemon_list:
        name = input("\n"f"Please enter a Pokemon's name: ").strip().lower()
        if name == '' or name not in pokemon_list:
            print('\nPlease enter a Gen 1 Pokemon name!')

    POKE_URL = f"https://pokeapi.co/api/v2/pokemon/{name}"
    pokemon = requests.get(POKE_URL).json()
    id = pokemon['id']
    moves = pokemon['moves']
    types = pokemon['types']
    pokename = string.capwords(name)

    type_list = []
    for typ in types:
        type_list.append(typ['type']['name'])

    move_list = []
    for move in moves:
        move_list.append(move['move']['name'])
    ascii(id)
    while True:
        info = input("\n"f"What would you like to know about {pokename}? (moves, id, type): ").strip().lower()
        clear()
        if info == 'moves' or info == 'move':
            ascii(id)
            print("\n"f"{pokename}'s list of moves: \n{move_list}")
        elif info == 'id':
            ascii(id)
            print("\n"f"{pokename}'s ID is: \n{id}")
        elif info == 'type' or info == 'types':
            ascii(id)
            print("\n"f"{pokename}'s type is: \n{type_list}")
        elif info == 'q' or info == 'quit':
            quit = input('\nAre you you sure you want to quit? (Y|N): ').strip().lower()
            if quit == 'y' or quit == 'yes':
                print('\nThank you for playing!')
                sys.exit()
            else:
                pass
        elif info == 'different' or info == 'new pokemon' or info == 'new':
            main()
        else:
            print('\nIncorrect Input')

if __name__ == "__main__":
    main()