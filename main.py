import book_ops
import data_file

# Setup the file first
data_file.check_file()

while True:
    print("\n")
    print("WELCOME TO LIBRARY SYSTEM")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search a Book")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        book_ops.add_book()
    elif choice == '2':
        book_ops.show_books()
    elif choice == '3':
        book_ops.search_book()
    elif choice == '4':
        print("Bye bye!")
        break
    else:
        print("Wrong choice. Try again.")