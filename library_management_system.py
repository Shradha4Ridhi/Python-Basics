# library_management_system.py

library = []

def add_book(book_name):
    library.append(book_name)
          print(f"'{book_name}' added to library.")

def remove_book(book_name):
    if book_name in library:
        library.remove(book_name)
          print(f"'{book_name}' removed from library.")
    else:
          print("Book not found.")

def view_books():
    if not library:
          print("Library is empty.")
        return

         print("\nBooks in Library:")
    for book in library:
         print("-", book)

if __name__ == "__main__":
    add_book("Python Basics")
    add_book("Data Science 101")

    view_books()
    remove_book("Python Basics")
    view_books()
