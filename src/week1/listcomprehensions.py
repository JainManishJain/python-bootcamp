# Task 1 : Given a list of numeric strings, convert them into integers. Using List Comprehensions
# strings = ["1", "2", "3", "4", "5"]
# Expected output : [1, 2, 3, 4, 5]

strings = ["1", "2", "3", "4", "5"]
result = [int(s) for s in strings]
print(result)


# Task 2 : Extract all integers from a list that are greater than 10. Using List Comprehensions
# numbers = [1, 5, 13, 4, 16, 7]
# Expected output :[13, 16]

numbers = [1, 5, 13, 4, 16, 7]
result = [num for num in numbers if num > 10]
print(result)


# Task 3 : Create a list of squares for numbers from 1 to 5. Using List Comprehensions
#Expected output :[1, 4, 9, 16, 25]

result = [i ** 2 for i in range(1, 6)]
print(result)


# Task 4 : Convert a 2D list into a 1D list.Using List Comprehensions
# matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
# Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
result = [num for row in matrix for num in row]
print(result)


# Task 5 : Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
# Expected output : {'a': 1, 'b': 2, 'c': 3}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)


# Task 6 : Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
# Expected output : {'Alice': 85, 'Charlie': 90}

scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
result = {name: score for name, score in scores.items() if score > 80}
print(result)

