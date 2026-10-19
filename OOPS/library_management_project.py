import json
import random
import string
from pathlib import Path
from datetime import datetime


class Library:

    database = "library.json"
    data = {"books" : [],"members": []}

    #load existing data to json or create your json
    if Path(database).exists():
        with open(database,"r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database,"w") as f:
            json.dum(data,f,indent = 4)

    def gen_id(prefix = "B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return prefix + "-" + random_id
    
    @classmethod
    def save_data(cls):
        with open(cls.database,"w") as f:
            json.dump(cls.data,f,indent =4, default = str)

    
    def add_book(self):
        title = input('enter book title: ')
        author = input("enter the book author: ")
        copies = int(input("how many copies: "))

        book = {
            "id" : Library.gen_id(),
            "title" : title,
            "author" : author,
            "total_copies": copies,
            "available_copies": copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        Library.data["books"].append(book)
        Library.save_data()


    def list_books(self):
        if not Library.data["books"]:
            print("sorry no books found")
            return
        for b in Library.data["books"]:
            print(f"{b['id']:12} {b['title'] [:24]:25} {b['author'][:19]:20} {b["total_copies"]}/{b["available_copies"]:>3}")

        print()

    def add_member(self):
        name = input("Enter the name:-")
        email = input('Enter the email:-')

        member = {
            "id" : Library.gen_id("M"),
            "name" : name,
            "email" : email,
            "borrowed" : []
        }

        Library.data['members'].append(member)
        Library.save_data()
        print("member added successfully")


    def list_member(self):
        if not Library.data['members']:
            print("there are no members")
            return
        for m in Library.data['members']:
            print(f"{m['id']:12} {m['name'][:24]:24} {m['email'][:20]:30}")
            print("this guy has currently ")
            print(f"{m["borrowed"]}")
        print()

    def borrow(self):
        member_id = input("Enter the member id:-").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("no such id exists")
            return
        member = members[0]

        book_id = input("Enter the book id:-").strip()
        books = [b for b in Library.data['books'] if b['id'] == book_id]
        if not books:
            print("no such id of book exist")
            return
        book = books[0]

        if book['available_copies'] <=0:
            print("sorry no book exist")
            return

        borrow_entry = {
            "book_id" : book['id'],
            'title':book['title'],
            'borrow_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        member['borrowed'].append("borrow_entry")
        book['available_copies'] -=1
        Library.save_data()




    

hello = Library()

print("="*50)
print("Library Management System")
print("="*50)
print("1. Add Book")
print("2. List Books")
print("3. Add Members")
print("4. List Members")
print("5. Borrow Book")
print("6. Return Book")
print("7. Exit The Portal")
print("="*50)

choice = input("What task you want to do: ")

if choice == "1":
    hello.add_book()

if choice == "2":
    hello.list_books()

if choice == "3":
    hello.add_member()

if choice == "4":
    hello.list_member()

if choice == "5":
    hello.borrow()

