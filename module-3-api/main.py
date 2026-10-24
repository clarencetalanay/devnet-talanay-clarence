import requests
import random

p1 = requests.get('https://pokeapi.co/api/v2/pokemon/p1')
p2 = requests.get('https://pokeapi.co/api/v2/pokemon/p2')
p3 = requests.get('https://pokeapi.co/api/v2/pokemon/p3')
p4 = requests.get('https://pokeapi.co/api/v2/pokemon/p4')
p5 = requests.get('https://pokeapi.co/api/v2/pokemon/p5')

name = p1.json()['name']
height = p1.json()['height']
weight = p1.json()['weight']

name = p2.json()['name']
height = p2.json()['height']
weight = p2.json()['weight']

name = p3.json()['name']
height = p3.json()['height']
weight = p3.json()['weight']

name = p3.json()['name']
height = p3.json()['height']
weight = p3.json()['weight']

name = p3.json()['name']
height = p3.json()['height']
weight = p3.json()['weight']

name = p3.json()['name']
height = p3.json()['height']
weight = p3.json()['weight']



random.choice
pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Meowth", "Froakie"]

input(print("Who's that Pokemon?"))
