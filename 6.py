employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for e in employees:
    print(f"{e[0]} is due is due to be paid {e[2]} USD by the end of the week")

total = 0

for i in employees:
    total += i[2]
avg = total/ len(employees)

for m in employees:
    if m[2] > avg:
        print(f"{m[0]} is earning {m[2]-avg}  USD more than average")
    elif m[2] < avg:
        print(f"{m[0]} is earning {avg - m[2]} USD less than average")
    else:
        print(f"{m[0]} is earning the average amount")