pets = []

def display_menu():
    print("""=== Pet Adoption Records ===
1. Add a pet
2. View all pets
3. Count available vs adopted
4. Find a pet by name
5. Exit""")
    pass

    choice = int(input("Choose an option:"))

def add_pet():
    petName = input("Pet name: ")
    petSpecies = input("Species: ")
    petStatus = input("Pet status: ")
    pet_list = petName + " - " + petSpecies + " - " + petStatus
    pets.append(pet_list)
    pass

def view_pets(pet_list):
    for x,y,z in pet_list.items():
        print(x,y,z)
    pass

def count_available_adopted(pet_list):
    for x in pet_list:
        break
    pass


def find_pet(pet_list):
    pass

def remove_pet(pet_list):
    pass

def main():
    running = True
    while running:
        choice = display_menu()
    if choice == 1:
        print("=== ADDING A PET ===")
        
    elif choice == 2:
        print("=== VIEW ALL PETS ===")
    elif choice == 3:
        print("=== SEE PET COUNT ===")
    elif choice == 4:
        print("=== FIND A PET ===")
    elif choice == 5:
        print("=== EXIT ===")
    else:
        print("Enter a valid choice of number")