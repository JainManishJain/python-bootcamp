# Task 1 : Find the Maximum and Minimum Values in a List

numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
maximum = max(numbers)
minimum = min(numbers)
print("Max:", maximum)
print("Min:", minimum)


# Task 2 : Given a set of numbers, find the maximum and minimum values.

setn = {5, 10, 3, 15, 2, 20}
maximum = max(setn)
minimum = min(setn)
print("Max:", maximum)
print("Min:", minimum)


# Task 3 : Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.

def shortest_and_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return shortest, longest

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = shortest_and_longest(words)
print(result)
