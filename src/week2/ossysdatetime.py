# Task 1 : Using datetime, add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time

from datetime import datetime, timedelta

original_dt = datetime(2020, 3, 22, 10, 0)
new_dt = original_dt + timedelta(weeks=1, hours=12)

print("Original datetime:", original_dt)
print("New datetime:", new_dt)


# Task 2 : Code to get the dates of yesterday, today, and tomorrow.

from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# Task 3 : Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.

import os

# Current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create folder "test"
os.mkdir("test")
print("Folder 'test' created")

# List files and folders
print("Directory contents:", os.listdir(cwd))

# Remove folder "test"
os.rmdir("test")
print("Folder 'test' removed")


# Task 4 : Write a Python program to rename a file from old_name.txt to new_name.txt.

import os

os.rename("old_name.txt", "new_name.txt")
print("File renamed successfully")


# Task 5 : Create a file and Write a Python program to get the size of a file named example.txt 

import os

# Create and write to file
with open("example.txt", "w") as file:
    file.write("Hello Python!")

# Get file size
size = os.path.getsize("example.txt")
print("File size:", size, "bytes")


# Task 6 : Convert the string "Feb 25 2020 4:20PM" into a Python datetime object

from datetime import datetime

dt = datetime.strptime("Feb 25 2020 4:20PM", "%b %d %Y %I:%M%p")
print(dt)


# Task 7 : Subtract 7 days from the date 2025-02-25 and print the result.

from datetime import datetime, timedelta

dt = datetime(2025, 2, 25)
new_dt = dt - timedelta(days=7)

print("New date:", new_dt.date())


# Task 8 : Format the date 2020-02-25 as "Tuesday 25 February 2020"

from datetime import datetime

dt = datetime(2020, 2, 25)
formatted_date = dt.strftime("%A %d %B %Y")

print(formatted_date)
