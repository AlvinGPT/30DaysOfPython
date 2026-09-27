import random
dividend = int(input("Please enter a number: "))
for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            print(f"{dividend} is not prime!")
            break
    else:
        print(f"{dividend} is prime!")
for j in range(1,101):
    if j.
for i in "Python":
    if i =="o":
        continue
    print(i)
randomno = random.randint(1,100)
while True:
    userno = int(input("Enter a number from 1 to 100"))
    if userno == randomno:
        break
        print("Correct")