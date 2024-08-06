class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed {self.title} by {self.author}.")
        else:
            print(f"{self.title} by {self.author} is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned {self.title} by {self.author}.")
        else:
            print(f"{self.title} by {self.author} is not borrowed.")


class Patron:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def register(self):
        print(f"Welcome, {self.name}! You have been registered.")

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"{book.title} by {book.author} is already borrowed.")
        else:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"You have borrowed {book.title} by {book.author}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"You have returned {book.title} by {book.author}.")
        else:
            print(f"You do not have {book.title} by {book.author} borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"{title} by {author} has been added to the library.")

    def register_patron(self, name, email):
        new_patron = Patron(name, email)
        self.patrons.append(new_patron)
        new_patron.register()

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

    def list_patrons(self):
        for patron in self.patrons:
            print(f"{patron.name} ({patron.email})")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Register a patron")
        print("3. List books")
        print("4. List patrons")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            name = input("Enter the name of the patron: ")
            email = input("Enter the email of the patron: ")
            library.register_patron(name, email)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            library.list_patrons()
        elif choice == '5':
            book_title = input("Enter the title of the book you want to borrow: ")
            for book in library.books:
                if book.title == book_title:
                    patron_name = input("Enter your name: ")
                    for patron in library.patrons:
                        if patron.name == patron_name:
                            patron.borrow_book(book)
                            break
                    else:
                        print("You are not a registered patron.")
                    break
            else:
                print("Book not found.")
        elif choice == '6':
            book_title = input("Enter the title of the book you want to return: ")
            for book in library.books:
                if book.title == book_title:
                    patron_name = input("Enter your name: ")
                    for patron in library.patrons:
                        if patron.name == patron_name:
                            patron.return_book(book)
                            break
                    else:
                        print("You are not a registered patron.")
                    break
            else:
                print("Book not found.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()