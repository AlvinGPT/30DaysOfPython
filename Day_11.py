"""Exercises
1) Create an empty set and assign it to a variable.

2) Add three items to your empty set using either several add calls, or a single call to update.

3) Create a second set which includes at least one common element with the first set.

4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

If you want an extra challenge, also tell the user if their number was too high or too low.

"""
#1
set1 = set()
#2
set1.update("Apple","Banana","Mango")
#3
set2 = {"Apple","Orange","Pineapple"}
#4
print(f"The Union of sets is {set1.union(set2)}")
print(f"The Symetric Difference of sets is {set1.symmetric_difference(set2)}")
print(f"The Intersection of sets is {set1.intersection(set2)}")
#5
list1 = []
for i in range(1,50):
    list1.append(i)

choice = int(input("Enter a Number: "))


if choice in list1:
    print(f"{choice} was the correct guess")
elif choice > j:
    print(f"{choice} was not the correct guess")