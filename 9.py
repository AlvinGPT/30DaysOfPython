tup = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name , ids ,(major , minor) = tup
print(f'''Name: {name}
ID: {ids}
Major: {major}
Minor: {minor}''')


main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
for char in main_characters:
    name , actor , species = char
    if species == "Human":
        print(f"{name} is a {species.lower()} played by {actor}")
    else:
        print(f"{name} is a {species.lower()} voiced by {actor}")