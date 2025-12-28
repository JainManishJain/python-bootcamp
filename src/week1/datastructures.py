# Task 1 : Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]
print("Max:", max(nums))
print("Min:", min(nums))


# Task 2 :Given two lists below, merge the values from both lists to one and print
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged_list = a + b
print(merged_list)


# Task 3. From a list, print the number of times the value 3 appears in the list:
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
count = a.count(3)
print("Number of times 3 appears:", count)


# Task 4. From below list, Sort the list and print
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
a.sort()
print(a)


# Task 5. Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)


# Task 6. Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)


# Task 7. Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1 & set2
print(intersection)


# Task 8. Given a tuple, count and print the number of occurrences of the element 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')
count = fruits.count('apple')
print("Apple count:", count)


# Task 9. Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)


# Task 10. Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["age"])


# Task 11. Add new key,  gender to dictionary and assign “M” to it and print
person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print(person)


# Task 12. Remove the key "city" from the above Dict and print
person = {"name": "Alice", "age": 30, "city": "New York"}
person.pop("city")
print(person)


# Task 13. Given two dictionaries, merge them into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)


