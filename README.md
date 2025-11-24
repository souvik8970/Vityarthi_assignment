# Library Management System

## Overview
This is a simple Python-based project designed to help librarians and students manage book records. It replaces manual note-keeping with a digital system that saves data permanently to a CSV file.

## Features
* **Add New Books:** Users can input details like Title, Author, and ISBN.
* **Search Books:** Allows finding a book by typing part of its title (e.g., "Harry" finds "Harry Potter").
* **View Inventory:** Displays a clean list of all books currently in the library.
* **Data persistence:** Automatically saves all records to `library.csv`, so data is not lost when the program closes.

## Technologies Used
* **Language:** Python 3.x
* **Libraries:** `csv` (for file handling), `os` (for checking file paths)
* **Tools:** VS Code / Notepad

## How to Install and Run
1.  **Download:** Download the project files (`main.py`, `book_ops.py`, etc.) to a folder on your computer.
2.  **Open Terminal:** Open Command Prompt or your IDE terminal in that folder.
3.  **Run:** Type the following command:
    ```bash
    python main.py
    ```
4.  **Use:** Follow the on-screen menu instructions (Type 1 to Add, 2 to View, etc.).

## Testing
I tested the project by:
1.  Adding a book and checking if it appears in the "View Inventory" list.
2.  Closing the program and restarting it to ensure the data was saved.
3.  Trying to search for a book that doesn't exist to make sure the program doesn't crash.
