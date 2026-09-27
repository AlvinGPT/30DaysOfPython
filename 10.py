tup = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )

song ={"Album Name" : tup[0],
       "The Artist": tup[1], 
       "Year" : tup[2], 
       "List" : tup[3]
}

for key, value in song.items():
    print(f"{key} : {value}")

del song["Year"]
song.update({"Date": "Mar 1 1973"})
print(song)
print(song.get("Year" ,"Unavailable"))