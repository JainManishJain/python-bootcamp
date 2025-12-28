# Task 1 :  Write a Python program to read the entire content of a file named sample.txt and display it.

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# Task 2 : Write a Python program to count the number of words in a file named words.txt

with open("words.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())

print("Total words:", word_count)


# Task 3 : Create a program to write the string “Hello, Python!” into a file named output.txt.

with open("output.txt", "w") as file:
    file.write("Hello, Python!")


# Task 4 : Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries

import csv

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
	

# Task 5 : From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.

def read_large_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line.strip()


for line in read_large_file("large_file.txt"):
    print(line)
