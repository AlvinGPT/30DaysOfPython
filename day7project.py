movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
for z in movies:
    print(f"Movie: {z[0]} \t Budget: {z[1]}")
choice = input("Do you want to add more? ").lower()
if choice == "yes":
    no = int(input("How many do you want to add? "))
    for s in range(1,no+1):
        name = input("What is the name of the movie? ")
        budget = int(input("What is the budget of the movie? "))
        movies.append((name,budget))
    print("New List")
    for d in movies:
        print(f"Movie: {d[0]} \t Budget: {d[1]}")
else:
    print("oki")
total_budget = 0
for i in movies:
    total_budget += i[1]
avg_budget = total_budget / len(movies)
noaboveavg = 0
print (f"The average budget is {avg_budget}")
for j in movies:
    if j[1] > avg_budget:
        print(f"{j[0]} is {j[1]-avg_budget} more than the average budget")
        noaboveavg += 1