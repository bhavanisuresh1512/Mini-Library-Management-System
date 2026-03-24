books = ["Python", "Java", "C++", "Data Science"]
borrowed = []
def menu():
    print("\nLibrary Menu")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
def get_choice():
    return input("Enter your choice: ")
def display_books(book_list):
    if len(book_list) == 0:
        print("No books available")
    else:
        print("\nAvailable Books:")
        for book in book_list:
            print(book)
def is_available(book, book_list):
    return book in book_list
def borrow_book(book, book_list=books, borrowed_list=borrowed):
    if is_available(book, book_list):
        book_list.remove(book)
        borrowed_list.append(book)
        print("Book borrowed successfully")
    else:
        print("Book not available")
def return_book(book, book_list, borrowed_list):
    if book in borrowed_list:
        borrowed_list.remove(book)
        book_list.append(book)
        return "Book returned successfully"
    else:
        return "Book not borrowed"
while True:
    menu()
    choice = get_choice()
    if choice == "1":
        display_books(books)
    elif choice == "2":
        book = input("Enter book name to borrow: ")
        borrow_book(book)
    elif choice == "3":
        book = input("Enter book name to return: ")
        result = return_book(book, books, borrowed)
        print(result)
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
