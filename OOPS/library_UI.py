# command for run this program
# python -m streamlit run library_UI.py
# python -m streamlit run OOPS/library_UI.py
import json
import random
import string
from pathlib import Path
from datetime import datetime
import streamlit as st
import pandas as pd


# ---------------- LIBRARY CLASS ----------------

class Library:

    database = str(Path(__file__).resolve().parent / "library.json")
    data = {"books": [], "members": []}

    # Load existing JSON data or create the file
    if Path(database).exists():
        with open(database, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def gen_id(prefix="B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(
                string.ascii_uppercase + string.digits
            )
        return prefix + "-" + random_id

    @classmethod
    def save_data(cls):
        with open(cls.database, "w", encoding="utf-8") as f:
            json.dump(cls.data, f, indent=4, default=str)

    # Same book creation logic; values come from Streamlit
    def add_book(self, title, author, copies):
        book = {
            "id": Library.gen_id(),
            "title": title,
            "author": author,
            "total_copies": copies,
            "available_copies": copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        Library.data["books"].append(book)
        Library.save_data()
        return book

    def list_books(self):
        return Library.data["books"]

    # Same member creation logic
    def add_member(self, name, email):
        member = {
            "id": Library.gen_id("M"),
            "name": name,
            "email": email,
            "borrowed": []
        }

        Library.data["members"].append(member)
        Library.save_data()
        return member

    def list_member(self):
        return Library.data["members"]

    # Same borrowing rules
    def borrow(self, member_id, book_id):
        members = [
            m for m in Library.data["members"]
            if m["id"] == member_id
        ]

        if not members:
            return False, "No such member ID exists."

        member = members[0]

        books = [
            b for b in Library.data["books"]
            if b["id"] == book_id
        ]

        if not books:
            return False, "No such book ID exists."

        book = books[0]

        if book["available_copies"] <= 0:
            return False, "Sorry, no copies are available."

        borrow_entry = {
            "book_id": book["id"],
            "title": book["title"],
            "borrow_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        member["borrowed"].append(borrow_entry)
        book["available_copies"] -= 1
        Library.save_data()

        return True, f"'{book['title']}' borrowed successfully."

    # Same return rules
    def return_book(self, member_id, choice):
        members = [
            m for m in Library.data["members"]
            if m["id"] == member_id
        ]

        if not members:
            return False, "No such member ID exists."

        member = members[0]

        if not member["borrowed"]:
            return False, "This member has no borrowed books."

        if choice < 1 or choice > len(member["borrowed"]):
            return False, "Invalid book selection."

        selected = member["borrowed"].pop(choice - 1)

        books = [
            bk for bk in Library.data["books"]
            if bk["id"] == selected["book_id"]
        ]

        if books:
            books[0]["available_copies"] += 1

        Library.save_data()

        return True, f"'{selected['title']}' returned successfully."


# ---------------- STREAMLIT UI ----------------

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)

library = Library()

st.sidebar.title("📚 My Library")
st.sidebar.caption("Library Management System")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Book",
        "List Books",
        "Add Member",
        "List Members",
        "Borrow Book",
        "Return Book"
    ]
)

books = Library.data["books"]
members = Library.data["members"]


# ---------------- DASHBOARD ----------------

if page == "Dashboard":
    st.title("📚 Library Management System")
    st.write("Welcome to your library dashboard!")

    total_books = sum(b["total_copies"] for b in books)
    available_books = sum(b["available_copies"] for b in books)
    borrowed_books = total_books - available_books

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Book Titles", len(books))
    c2.metric("Total Copies", total_books)
    c3.metric("Available Copies", available_books)
    c4.metric("Members", len(members))

    st.subheader("📖 Recent Books")

    if books:
        st.dataframe(
            pd.DataFrame([
                {
                    "Book ID": b["id"],
                    "Title": b["title"],
                    "Author": b["author"],
                    "Total Copies": b["total_copies"],
                    "Available Copies": b["available_copies"]
                }
                for b in reversed(books[-5:])
            ]),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No books found. Add your first book.")

    st.caption(f"Currently borrowed copies: {borrowed_books}")


# ---------------- ADD BOOK ----------------

elif page == "Add Book":
    st.title("➕ Add a New Book")

    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        copies = st.number_input(
            "Number of Copies",
            min_value=1,
            step=1,
            value=1
        )

        submitted = st.form_submit_button(
            "Add Book",
            use_container_width=True
        )

    if submitted:
        if not title.strip() or not author.strip():
            st.error("Please enter the book title and author.")
        else:
            book = library.add_book(
                title.strip(),
                author.strip(),
                int(copies)
            )
            st.success(f"Book added successfully! ID: {book['id']}")


# ---------------- LIST BOOKS ----------------

elif page == "List Books":
    st.title("📚 All Books")

    if not books:
        st.info("Sorry, no books found.")
    else:
        search = st.text_input("🔍 Search books")

        filtered = [
            b for b in books
            if search.lower() in b["title"].lower()
            or search.lower() in b["author"].lower()
            or search.lower() in b["id"].lower()
        ]

        st.dataframe(
            pd.DataFrame([
                {
                    "Book ID": b["id"],
                    "Title": b["title"],
                    "Author": b["author"],
                    "Total Copies": b["total_copies"],
                    "Available Copies": b["available_copies"],
                    "Added On": b.get("added_on", "")
                }
                for b in filtered
            ]),
            use_container_width=True,
            hide_index=True
        )


# ---------------- ADD MEMBER ----------------

elif page == "Add Member":
    st.title("👤 Register a Member")

    with st.form("add_member_form"):
        name = st.text_input("Member Name")
        email = st.text_input("Email Address")

        submitted = st.form_submit_button(
            "Register Member",
            use_container_width=True
        )

    if submitted:
        if not name.strip() or not email.strip():
            st.error("Please enter the name and email.")
        else:
            member = library.add_member(name.strip(), email.strip())
            st.success(
                f"Member added successfully! ID: {member['id']}"
            )


# ---------------- LIST MEMBERS ----------------

elif page == "List Members":
    st.title("👥 All Members")

    if not members:
        st.info("There are no members.")
    else:
        st.dataframe(
            pd.DataFrame([
                {
                    "Member ID": m["id"],
                    "Name": m["name"],
                    "Email": m["email"],
                    "Borrowed Books": len(m["borrowed"])
                }
                for m in members
            ]),
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Member Borrowing Details")

        selected_member = st.selectbox(
            "Select Member",
            members,
            format_func=lambda m: f"{m['name']} ({m['id']})"
        )

        if selected_member["borrowed"]:
            st.dataframe(
                pd.DataFrame(selected_member["borrowed"]),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("This member has no borrowed books.")


# ---------------- BORROW BOOK ----------------

elif page == "Borrow Book":
    st.title("📥 Borrow a Book")

    if not members:
        st.warning("Please add a member first.")
    elif not books:
        st.warning("Please add a book first.")
    elif not any(b["available_copies"] > 0 for b in books):
        st.warning("No copies are currently available.")
    else:
        with st.form("borrow_form"):
            selected_member = st.selectbox(
                "Select Member",
                members,
                format_func=lambda m: f"{m['name']} ({m['id']})"
            )

            available = [
                b for b in books
                if b["available_copies"] > 0
            ]

            selected_book = st.selectbox(
                "Select Book",
                available,
                format_func=lambda b: (
                    f"{b['title']} — {b['author']} "
                    f"({b['available_copies']} available)"
                )
            )

            submitted = st.form_submit_button(
                "Borrow Book",
                use_container_width=True
            )

        if submitted:
            success, message = library.borrow(
                selected_member["id"],
                selected_book["id"]
            )

            if success:
                st.success(message)
            else:
                st.error(message)


# ---------------- RETURN BOOK ----------------

elif page == "Return Book":
    st.title("📤 Return a Book")

    members_with_books = [
        m for m in members if m["borrowed"]
    ]

    if not members_with_books:
        st.info("No members currently have borrowed books.")
    else:
        selected_member = st.selectbox(
            "Select Member",
            members_with_books,
            format_func=lambda m: f"{m['name']} ({m['id']})"
        )

        borrowed = selected_member["borrowed"]

        # Display the borrowed books
        st.dataframe(
            pd.DataFrame([
                {
                    "Number": i,
                    "Book ID": b["book_id"],
                    "Title": b["title"],
                    "Borrowed On": b.get("borrow_on", "")
                }
                for i, b in enumerate(borrowed, start=1)
            ]),
            use_container_width=True,
            hide_index=True
        )

        with st.form("return_form"):
            choice = st.selectbox(
                "Select Book to Return",
                range(1, len(borrowed) + 1),
                format_func=lambda i: (
                    f"{i}. {borrowed[i - 1]['title']} "
                    f"({borrowed[i - 1]['book_id']})"
                )
            )

            submitted = st.form_submit_button(
                "Return Book",
                use_container_width=True
            )

        if submitted:
            success, message = library.return_book(
                selected_member["id"],
                choice
            )

            if success:
                st.success(message)
            else:
                st.error(message)
