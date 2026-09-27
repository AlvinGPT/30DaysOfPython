'''For this project the application needs to have the following functionality:

Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
The program should store information about all of these books in a Python list.
Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).
This project is a bit larger than the ones we've tackled before, so make sure you tackle it one piece at a time.

Something to note with this project is that because the books in the reading list are stored in a Python list, when the program ends, the reading list data will be lost.

In a couple of days, in Day 14, we will come back to this project and expand it, making sure we don't lose data when the program ends!

'''
reading_list = []

def add_books(title,name,year):
    reading_list.append({"title": title, "name": name, "year": year})
    print("Book Added")
def print_all_books():
    for book in reading_list:
        print(f"Book Title: {book["title"]} \n Author's Name: {book["name"]} \n Year of Publication: {book["year"]}")
def remove_books(title,name,year):
    count = 0
    for index,book in enumerate(reading_list):
        if book == {"title": title, "name": name, "year": year}:
            del reading_list[index]
            print("Book Removed")
        else:
            count += 1
    if count == len(reading_list):
        print("Book Not Present")
while True:
    
    print("""
    1. Add Books
    2. Show All Books
    3. Remove a Book""")
    choice = int(input("Chose a Number: "))
    if choice == 1:
        title = input("Enter the Title of the Book: ").title()
        name = input("Enter the Name of the Author: ").title()
        year = int(input("Enter the Year of Publication: "))
        add_books(title,name,year)
    elif choice == 2:
        print_all_books()
    elif choice == 3:
        title = input("Enter the Title of the Book: ").title()
        name = input("Enter the Name of the Author: ").title()
        year = int(input("Enter the Year of Publication: "))
        remove_books(title,name,year)
    else:
        print("Invalid Option, Try Again")
        continue