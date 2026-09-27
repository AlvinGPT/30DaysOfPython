card = input("Enter card no: ").strip()
cardlist =[]
for i in card:
    cardlist.append(int(i))
lastdigit = cardlist[-1]
del cardlist[-1]
cardlist = cardlist[::-1]
for j in range(0,len(cardlist)+1, 2):
    cardlist[j] = cardlist[j]*2
    if cardlist[j] > 9:
        cardlist[j] -= 9
final = sum(cardlist) + lastdigit
if final % 10 == 0:
    print(f"{card} is a valid card number")
else:
    print(f"{card} is not a valid card number")