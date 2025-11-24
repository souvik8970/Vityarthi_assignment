# Problem Statement
Managing library records manually in notebooks is time-consuming and error-prone. It is difficult to search for specific books or track inventory accurately without a digital system.

# Scope
This project is a text-based (console) application developed in Python. It focuses on the core operations of a library, such as adding new books and searching for them. It uses a CSV file for data storage instead of a complex database, making it lightweight and easy to use.

# Target Users
* **Librarians:** To manage the book inventory and add new arrivals.
* **Students/Users:** To check if a specific book is available in the library.

# High-Level Features
* **Add Books:** Allows the user to input book details (Title, Author, ISBN) and saves them.
* **View Inventory:** Displays a complete list of all books currently in the library.
* **Search Functionality:** Enables users to find a book by entering its title.
* **Data Persistence:** Automatically saves all data to `library.csv` so records are not lost when the program closes.
