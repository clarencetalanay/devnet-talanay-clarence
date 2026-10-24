import requests
import random

p1 = requests.get('https://pokeapi.co/api/v2/pokemon/p1')
p2 = requests.get('https://pokeapi.co/api/v2/pokemon/p2')
p3 = requests.get('https://pokeapi.co/api/v2/pokemon/p3')
p4 = requests.get('https://pokeapi.co/api/v2/pokemon/p4')
p5 = requests.get('https://pokeapi.co/api/v2/pokemon/p5')

name = ['name']
height = ['height']
weight = ['weight']


pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Meowth", "Froakie"]
pnames = random.choice
input(print("Who's that Pokemon?"))
