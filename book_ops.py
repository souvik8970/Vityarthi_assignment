import data_file

def add_book():
    print("--- Add New Book ---")
    b_id = input("Enter Book ID: ")
    b_name = input("Enter Book Name: ")
    b_auth = input("Enter Author: ")
    b_qty = input("Enter Quantity: ")

    # loading current data
    all_books = data_file.read_data()
    
    # appending the new book to the list
    new_book = [b_id, b_name, b_auth, b_qty]
    all_books.append(new_book)
    
    # saving back to file
    data_file.write_data(all_books)
    print("Book saved successfully!")

def show_books():
    print("--- List of Books ---")
    all_books = data_file.read_data()
    
    # Simple loop to print items
    # skipping index 0 because it is the header
    for i in range(1, len(all_books)):
        row = all_books[i]
        print("ID:", row[0], " | Name:", row[1], " | Qty:", row[3])

def search_book():
    search_id = input("Enter Book ID to search: ")
    all_books = data_file.read_data()
    
    found = False
    for row in all_books:
        if row[0] == search_id:
            print("Found it! Book:", row[1], "by", row[2])
            found = True
            break
            
    if found == False:
        print("Book not found.")