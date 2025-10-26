class Book:
    # Represents a single book in the library.
    def __init__(self, title, author):
        self.title = title # Public attribute
        self.author = author # Public attribute
        self._is_checked_out = False # Private attribute (starts as available)
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # already available
    
    def is_available(self):
        # Returns True if the book is not checked out.
        return not self._is_checked_out

    def __str__(self):
        # Provides a user-friendly string representation of the book.
        return f"{self.title} by {self.author}"

class Library:
    # Represents a collection of books and operations on them.
    def __init__(self):
        self._books = [] # Private list of Book objects
    
    def add_book(self, book):
        # Adds a new Book object to the library.
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
            print(f"'{title}' is not available or doesn’t exist.")
            return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
            print(f"'{title}' was not checked out or doesn’t exist.")
            return False   

    def list_available_books(self):
        # Prints all available books.
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")