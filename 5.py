#1
a =["hi", "hallo","good bye"]
b =["hi", "hallo","good bye"]
print(id(a)==id(b))
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers = [1, 2, 3, 4]
numbers.append(5)
print(new_numbers is numbers)

num =int(input("Enter a Integer: "))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")


wage = float(input("Enter your Hourly wage: "))
hours = float(input("Enter the Number of Hours you worked: "))

if hours > 40:
    print(f"You are due for an overtime payment of {(hours - 40)*(0.10* wage)} USD")