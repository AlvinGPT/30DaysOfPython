#1
movies = [
    (
        "asdfghjkl",
        "qwertyuy",
        572,
        3456789
    )
]
print(movies)
name = input("What is the the name of the movie? ").strip().title()
direc = input("What is the the name of the director? ").strip().title()
year = int(input("What is the the release year of the movie? "))
budget = float(input("What is the the budget of the movie? "))
movie = (name,direc,year,budget)
print(movie[0],movie[2])
movies.append(movie)
print(movies)
del movies[0]
print(movies)
