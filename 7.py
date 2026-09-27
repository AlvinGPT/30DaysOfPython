word= input("Enter a word/phrase: ").strip(" ")
print(len(word))
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
quotes1 = quotes[0].strip("'")
quotes2 = quotes[1].strip("'")
quotes3 = quotes[2].strip("'")
quotes4 = quotes[3].strip("'")
print(quotes1,quotes2,quotes3,quotes4,sep ="\n")
name = input("Enter your full name: ")
names =[]
name = name.split(" ")

print(name)

numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(' | '.join(stringified_numbers)) # 1, 2, 3, 4, 5