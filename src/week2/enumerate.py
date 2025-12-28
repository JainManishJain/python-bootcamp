# Task 1 : Using below list and enumerate(), print index followed by value. 

fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)


# Task 2 : Using below dict and enumerate, print key followed by value

person = {"name": "Alice", "age": 30, "city": "New York"}
for _, key in enumerate(person):
    print(f"{key}: {person[key]}")


# Task 3 : Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.
   
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
result = [(index, fruit) for index, fruit in enumerate(fruits, start=1) if index % 2 == 0]
print(result)
  


