import requests
import random

pokemon_list = ["bulbasaur", "charmander", "squirtle", "meowth", "froakie"]
pokemon_data = {}

for name in pokemon_list:
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    data = pokemon.json()
    pokemon_data[name] = {
        "name": data["name"].capitalize(),
        "height": data["height"],
        "weight": data["weight"]
    }

choice = random.choice(list(pokemon_data.keys()))
poke = pokemon_data[choice]

print("---Who's that Pokémon?---")
print(f"Height: {poke['height']}")
print(f"Weight: {poke['weight']}")
print("\nChoices: bulbasaur, charmander, squirtle, meowth, froakie")

win = False
for attempt in range(1, 4):
    guess = input(f"\nAttempt {attempt}/3 - Enter your guess: ")
    
    if guess not in pokemon_list:
        print("\nINVALID POKEMON NAME! Try again.")
        print(f"Height: {poke['height']}")
        print(f"Weight: {poke['weight']}")
        print("\nChoices: bulbasaur, charmander, squirtle, meowth, froakie")
        continue
        
    if guess == poke['name'].lower():
        print(f"CORRECT! It's {poke['name']}!")
        win = True
        break
    else:
        print("\nINCORRECT GUESS!")
        print(f"Height: {poke['height']}")
        print(f"Weight: {poke['weight']}")
        print("\nChoices: bulbasaur, charmander, squirtle, meowth, froakie")

if not win:
    print(f"\nGame Over! The correct Pokémon was {poke['name']}.")