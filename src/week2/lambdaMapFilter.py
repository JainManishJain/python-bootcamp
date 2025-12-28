# Task 1 : Given a list let's see how to double each element of the given list. Using map() 

a = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, a))
print(result)


# Task 2 : Use filter() and lambda to extract all even numbers from a list of integers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


# Task 3 : Use reduce() and lambda to find the longest word in a list of strings.

from functools import reduce

words = ["apple", "banana", "cherry", "date"]

longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)


# Task 4 : Use map() to square each number in the list and round the result to one decimal place.

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

result = list(map(lambda x: round(x ** 2, 1), my_floats))
print(result)


# Task 5 : Use filter() to select names with 7 or fewer characters from the list.

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

result = list(filter(lambda name: len(name) <= 7, my_names))
print(result)


# Task 6 : Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)
print(total)
