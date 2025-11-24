import csv
import os

# This is the path where my data will be saved
file_path = "data/library.csv"

def check_file():
    # Check if file exists, if not create it
    if not os.path.exists("data"):
        os.makedirs("data") # make the folder if missing
    
    if not os.path.exists(file_path):
        f = open(file_path, "w", newline="")
        writer = csv.writer(f)
        # Adding the headings
        writer.writerow(["ID", "Name", "Author", "Count"])
        f.close()

def read_data():
    # Reading all rows from the csv file
    data = []
    if os.path.exists(file_path):
        f = open(file_path, "r")
        reader = csv.reader(f)
        data = list(reader) # convert to a list
        f.close()
    return data

def write_data(all_rows):
    # Overwriting the file with new data
    f = open(file_path, "w", newline="")
    writer = csv.writer(f)
    writer.writerows(all_rows)
    f.close()